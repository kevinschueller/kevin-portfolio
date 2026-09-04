// @ts-check
import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const projects = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/projects' }),
  schema: z.object({
    title: z.string(),
    subtitle: z.string().default(''),
    pubDate: z.coerce.date().optional(),
    thumb: z.string().optional(),
    contentImg: z.string().optional(),
  }),
});

const posts = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/posts' }),
  schema: z.object({
    title: z.string(),
    subtitle: z.string().default(''),
    pubDate: z.coerce.date(),
    thumb: z.string().optional(),
    contentImg: z.string().optional(),
    excerpt: z.string().default(''),
  }),
});

export const collections = { projects, posts };
