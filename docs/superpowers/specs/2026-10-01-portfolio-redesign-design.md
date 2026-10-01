# Personal portfolio redesign

## Goal

Turn the site into a complete portfolio structure for `xufilps`, with clear routes to projects, writing, and personal information. The design uses no personal claims, projects, articles, photos, or contact details that the owner has not supplied.

## Information architecture

- Home: identity and purpose, featured project area, writing area, and a small contact rail.
- Projects: a reusable project entry format and an honest empty state.
- Writing: a reusable article list format and an honest empty state.
- About: space for a biography, practice, and contact details, all clearly awaiting real content.
- Existing notes remain in Git but are not presented as published portfolio content. Old `now`, `things`, `links`, and `notes` HTML pages leave the navigation.

## Visual and interaction design

- A quiet editorial layout with a compact masthead, generous type hierarchy, thin dividers, a desktop primary column and supporting rail, and a single column on narrow screens.
- A light and dark color scheme. A small script handles the theme button, respects system preference on first visit, and persists the visitor's choice when storage is available.
- Semantic HTML contains all visible content. JavaScript is not required to read or navigate the site.
- Responsive typography, keyboard focus, skip link, active navigation state, and reduced motion support.

## Content rules

- The public handle `xufilps` can identify the site; it does not stand in for an unprovided personal name.
- Empty areas state plainly what is missing, without fake cards, invented credentials, dates, or contact methods.
- HTML comments explain where genuine project, article, biography, and contact content can be added.

## Delivery and boundaries

Use native HTML, CSS, and a small JavaScript file, with no framework, build step, remote assets, or analytics. Work on `feat/portfolio-redesign-20261001`; preserve the pre-existing deletion of `docs/project-plan.md` as an unrelated working-tree change. Verify every route, theme behavior, responsive layout, and repository diff before committing only redesign files. Do not publish or push in this task.
