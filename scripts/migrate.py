#!/usr/bin/env python3
"""Migrate kevin-portfolio Stackbit content -> Astro content collections."""
import os, re, glob, shutil, unicodedata, json
from datetime import datetime
import yaml

SRC = "/Users/kevinschueller/projects/kevin-portfolio"
DST = "/Users/kevinschueller/projects/kevin-portfolio-rebuild"
OLD_PAGES = os.path.join(SRC, "src/pages")
STATIC = os.path.join(SRC, "static")


def slugify(s):
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return re.sub(r"-+", "-", s)


def parse_old(path):
    txt = open(path).read()
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", txt, re.S)
    if not m:
        return {}, ""
    return yaml.safe_load(m.group(1)) or {}, m.group(2).strip()


def dt(v):
    if isinstance(v, datetime):
        return v
    if v is None:
        return None
    s = str(v).strip()
    if not s:
        return None
    try:
        return datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        pass
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d")
    except ValueError:
        return None


def write_md(path, frontmatter, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    out = ["---"]
    for k, v in frontmatter.items():
        if v is None:
            continue
        out.append(yaml.safe_dump({k: v}, default_flow_style=False,
                                  allow_unicode=True, width=10**6,
                                  sort_keys=False).rstrip("\n"))
    out.append("---")
    out.append("")
    out.append(body.strip())
    with open(path, "w") as f:
        f.write("\n".join(out) + "\n")


# ---------- copy assets ----------
shutil.rmtree(os.path.join(DST, "public/images"), ignore_errors=True)
os.makedirs(os.path.join(DST, "public/images"), exist_ok=True)
copied = 0
for root, dirs, files in os.walk(os.path.join(STATIC, "images")):
    for f in files:
        if f.startswith("."):
            continue
        shutil.copy2(os.path.join(root, f),
                     os.path.join(DST, "public/images", f))
        copied += 1
print("copied %d images" % copied)

# ---------- read content ----------
projects, posts, pages = [], [], []
for p in sorted(glob.glob(os.path.join(OLD_PAGES, "projects", "*.md"))):
    fm, body = parse_old(p)
    projects.append((p, fm, body))
for p in sorted(glob.glob(os.path.join(OLD_PAGES, "posts", "*.md"))):
    fm, body = parse_old(p)
    posts.append((p, fm, body))
for p in sorted(glob.glob(os.path.join(OLD_PAGES, "*.md"))) + \
         sorted(glob.glob(os.path.join(OLD_PAGES, "*", "index.md"))):
    fm, body = parse_old(p)
    pages.append((p, fm, body))

print("found %d projects, %d posts, %d pages" % (len(projects), len(posts), len(pages)))

# ---------- projects ----------
os.makedirs(os.path.join(DST, "src/content/projects"), exist_ok=True)
for path, fm, body in projects:
    slug = slugify(fm.get("title", os.path.basename(path)))
    write_md(os.path.join(DST, "src/content/projects", slug + ".md"), {
        "title": fm.get("title"),
        "subtitle": fm.get("subtitle") or "",
        "pubDate": dt(fm.get("date")),
        "thumb": fm.get("thumb_img_path"),
        "contentImg": fm.get("content_img_path"),
    }, body)

# ---------- posts ----------
os.makedirs(os.path.join(DST, "src/content/posts"), exist_ok=True)
for path, fm, body in posts:
    slug = slugify(fm.get("title", os.path.basename(path)))
    write_md(os.path.join(DST, "src/content/posts", slug + ".md"), {
        "title": fm.get("title"),
        "subtitle": fm.get("subtitle") or "",
        "pubDate": dt(fm.get("date")),
        "thumb": fm.get("thumb_img_path"),
        "contentImg": fm.get("content_img_path"),
        "excerpt": fm.get("excerpt") or "",
    }, body)

# fix body image refs (already same path; kept for future transforms)
for f in glob.glob(os.path.join(DST, "src/content", "**", "*.md"), recursive=True):
    txt = open(f).read()

# ---------- pages ----------
def page_record(path, fm, body, slug):
    menus = fm.get("menus") or {}
    main = menus.get("main") or {}
    return {
        "slug": slug,
        "title": fm.get("title"),
        "subtitle": fm.get("subtitle") or "",
        "menuTitle": main.get("title"),
        "menuWeight": main.get("weight"),
        "img": fm.get("img_path") or "",
        "template": fm.get("template"),
        "body": body,
    }

pages_out = []
for path, fm, body in pages:
    if path.endswith("index.md"):
        slug = os.path.basename(os.path.dirname(path))
        if slug == "pages":
            slug = "home"
    else:
        slug = slugify(fm.get("title", os.path.basename(path)))
    pages_out.append(page_record(path, fm, body, slug))

# ---------- index sections -> site data ----------
index = next(p for p in pages if p[0].endswith(os.path.join("pages", "index.md")))
ifm = index[1]
hero = services = testimonials = projects_pref = posts_pref = None
for sec in ifm.get("sections", []):
    t = sec.get("type")
    if t == "heroblock":
        hero = sec
    elif t == "servicesblock":
        services = sec
    elif t == "testimonialsblock":
        testimonials = sec
    elif t == "portfolioblock":
        projects_pref = sec
    elif t == "postsblock":
        posts_pref = sec

site_data = {
    "title": "Kevin Schueller",
    "description": "Designer & developer - interactive experiences and products.",
    "email": "kevinschueller@gmail.com",
    "hero": {"title": hero["title"], "content": hero["content"]},
    "services": [{"title": s["title"], "content": s["content"]}
                 for s in services["serviceslist"]],
    "testimonials": [{"author": t["author"],
                      "avatar": t["avatar"],
                      "content": t["content"].strip()}
                     for t in testimonials["testimonialslist"]],
    "portfolioSection": {"title": projects_pref["title"],
                         "subtitle": projects_pref["subtitle"],
                         "num": projects_pref.get("num_projects_displayed", 4)},
    "postsSection": {"title": posts_pref["title"],
                     "subtitle": posts_pref.get("subtitle", ""),
                     "num": posts_pref.get("num_posts_displayed", 2)},
}
os.makedirs(os.path.join(DST, "src/data"), exist_ok=True)
with open(os.path.join(DST, "src/data/site.json"), "w") as f:
    json.dump(site_data, f, indent=2, ensure_ascii=False)
print("wrote src/data/site.json")

for t in site_data["testimonials"]:
    fn = os.path.basename(t["avatar"])
    ok = os.path.exists(os.path.join(DST, "public/images", fn))
    print("  avatar", fn, "OK" if ok else "MISSING")

# save pages_out for the page-writer step
with open(os.path.join(DST, "scripts", "pages_out.json"), "w") as f:
    json.dump(pages_out, f, indent=2, ensure_ascii=False)
print("pages_out slugs:", [p["slug"] for p in pages_out])
