---
title: Home
sections:
- type: heroblock
  template: heroblock
  title: Hi, I'm Kevin Schueller
  section_id: hero
  component: HeroBlock
  content: I'm a digital designer and web developer with over 10 years of experience
    designing and developing interactive experiences.
- type: portfolioblock
  template: portfolioblock
  title: Recent Work
  section_id: latest-projects
  component: PortfolioBlock
  subtitle: Some recent projects that I designed
  layout_style: mosaic
  num_projects_displayed: 6
  view_all_text: View All
  view_all_url: portfolio/index.html
- type: servicesblock
  template: servicesblock
  title: Designer's Toolkit
  section_id: services
  component: ServicesBlock
  subtitle: Tools I use and am an expert with
  serviceslist:
  - title: Adobe Creative Suite
    content: I'm an expert in Photoshop, InDesign, AfterEffects, XD, Illustrator,
      and Animate.
  - title: Wireframing and Prototyping
    content: I've use Adobe Comp, Figma, Sketch, and Adobe XD to rapidly prototype
      designs and wireframes.
  - title: HTML5, CSS, JavaScript
    content: I'm an expert in HTML5, CSS, and I'm currently completing an advanced
      online JavaScript course and have written extensive JQuery code. I've also worked
      with other frameworks like React and Vue.
  - title: Service title
    content: Aliquam pulvinar, orci ac scelerisque tempus, felis leo sagittis justo,
      sit amet condimentum lorem nibh vel quam. Duis consectetur lorem ipsum, non
      efficitur urna viverra et.
- type: testimonialsblock
  template: testimonialsblock
  title: Testimonials
  section_id: testimonials
  component: TestimonialsBlock
  subtitle: An optional subtitle of the section
  testimonialslist:
  - author: John Doe
    avatar: images/john_doe.jpg
    content: Vestibulum a nunc ut eros condimentum posuere. Nullam dapibus quis nunc
      non interdum. Pellentesque tortor ligula, gravida ac commodo eu.
  - author: Jane Roe
    avatar: images/jane_roe.jpg
    content: Sed laoreet magna commodo libero euismod sodales. Nunc ac libero convallis,
      interdum ligula vel, pretium diam. Integer commodo sem at dui sollicitudin,
      vel posuere justo laoreet.
- type: postsblock
  template: postsblock
  title: Latest from the Blog
  section_id: latest-posts
  component: PostsBlock
  subtitle: An optional subtitle of the section
  num_posts_displayed: 2
  actions:
  - label: View Blog
    url: blog/index.html
- type: contactblock
  template: contactblock
  title: Contact Us
  section_id: contact
  component: ContactBlock
  subtitle: An optional subtitle of the section
menus:
  main:
    title: Home
    weight: 1
template: home

---
