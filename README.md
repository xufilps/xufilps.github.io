# A Small Corner

A quiet personal homepage: a place to write, collect things, and leave room for the site to grow. It is plain HTML and CSS, with no framework, build step, or external dependencies.

## Preview locally

From this folder, run:

```sh
python3 -m http.server 8000
```

Then open <http://localhost:8000>. Stop the server with `Ctrl+C`.

## Publish with GitHub Pages

1. Create a GitHub repository for this site and push this folder to it.
2. In the repository, open **Settings → Pages**.
3. Under **Build and deployment**, choose **Deploy from a branch**, select `main` and `/ (root)`, then save.
4. GitHub Pages will show the published address in the same settings page. A custom domain can be connected there later.

All internal links and styles use relative paths, so they work on a project site as well as a custom domain. Nothing has been pushed or published from this local copy.

## Where to add your own content

- `index.html`: name, short introduction, and home-page summaries.
- `now/index.html`: current interests and activities.
- `notes/index.html`: add links to notes as you write them; each note can be a new folder with an `index.html` page.
- `things/index.html`: add only things you want to share. Each entry can include an image, name, date, and one-sentence description.
- `links/index.html`: add links and your own short notes under the groups.
- `about/index.html`: replace the prompts with whatever you want people to know.
- `styles.css`: shared colors, spacing, typography, and responsive layout.

The site's working title is **a small corner**. Change it in the page headers and titles whenever a better name comes along.
