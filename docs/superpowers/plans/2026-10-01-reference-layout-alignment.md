# Reference layout alignment plan

## Goal and scope

Bring all four public pages as close as practical to the structure and spacing of the local `lizaixi01.github.io` reference. Preserve the owner's `xufilps` identity and honest empty states; do not reuse the reference owner's portrait, biography, project claims, article text, or contact details.

## Files and tasks

1. Rework `index.html` around the reference's compact identity header, left content column (About, featured project, essays), and right contact rail. Match navigation order and add the verified GitHub profile link. Use a labeled monogram placeholder where the reference has a portrait.
2. Rework `projects/index.html`, `writing/index.html`, and `about/index.html` to match the reference's page intro, project grid, article controls/list, and two-column About layout. Keep empty states visibly empty.
3. Replace `styles.css` with a focused stylesheet using the reference's page width, serif hierarchy, divider rhythm, warm palette, responsive breakpoints, row treatments, and dark colors. Adapt rather than copy unrelated SPA and article-case styles.
4. Update `theme.js` label and `README.md` editing guidance, then review all four pages in a browser at desktop and phone widths.

## Verification and risks

- Check one H1, four nav links with one current page, local paths, theme persistence, keyboard focus, and no horizontal overflow on each route.
- Compare same-size screenshots of the reference and local pages, then run `git diff --check` and JS syntax check.
- Preserve the pre-existing staged deletion of `docs/project-plan.md`; commit only this alignment's files.
- A portrait, finished project entries, articles, and public contact details cannot visually match populated reference content until the owner supplies them.

## Rollback and delivery

Work on `feat/reference-layout-alignment`, then fast-forward `main` and push after checks using the user's standing publication request. Revert the alignment commit to restore the previous layout if needed.

## Browser comment follow-up

On `fix/mobile-title-and-profile-placeholders`, make the project heading break after its comma at phone widths, replace both portrait monograms with one local white image, and change the About profile fields to education, interests, and contact channels. Check phone and desktop layout, image loading in both themes, and local paths before publishing to `main`; preserve the staged plan deletion. Revert this follow-up commit to roll back these changes.
