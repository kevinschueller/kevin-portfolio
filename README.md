# kevin-portfolio v2 — Astro

Kevin Schueller's portfolio, rebuilt on Astro 5 (Sept 2026) from the original
Gatsby 2 / Stackbit site. All legacy content and URLs are preserved.

## Stack

- Astro 5, zero-JS static output
- Content: markdown collections (`src/content/projects`, `src/content/posts`)
- Fonts: self-hosted variable Inter + Fraunces
- Hosting: Netlify (`netlify.toml` — redirects from all legacy URLs, security headers)
- Forms: Netlify Forms (`contact` form on `/` and `/contact/`)

## Commands

| command         | what                  |
| --------------- | --------------------- |
| `npm run dev`   | local dev server      |
| `npm run build` | build to `dist/`      |
| `npm run preview` | serve the build     |

## Editing content

- **Projects**: add a `.md` file to `src/content/projects/` with `title`,
  `subtitle`, `pubDate`, `thumb`, `contentImg` frontmatter
- **Posts**: add a `.md` file to `src/content/posts/` with `title`, `subtitle`,
  `pubDate`, `thumb`, `contentImg`, `excerpt`
- **Home sections** (hero, services, testimonials): `src/data/site.json`
- Images go in `public/images/` and are referenced as `/images/<name>`
