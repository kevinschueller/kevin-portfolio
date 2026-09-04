import rss from '@astrojs/rss';
import { getCollection } from 'astro:content';

export async function GET(context) {
  const posts = await getCollection('posts');
  return rss({
    title: 'Kevin Schueller — Blog',
    description: 'Notes on design, development, and building for the web.',
    site: context.site,
    items: posts
      .sort((a, b) => b.data.pubDate.getTime() - a.data.pubDate.getTime())
      .map((post) => ({
        title: post.data.title,
        description: post.data.excerpt || post.data.subtitle,
        pubDate: post.data.pubDate,
        link: `/posts/${post.id}/`,
      })),
    customData: '<language>en-us</language>',
  });
}
