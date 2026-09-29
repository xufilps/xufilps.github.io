# Personal Corner Website v0.1 — Project Plan

## Goal
Create a quiet, minimal personal homepage that can grow over time. This is a personal space, not a portfolio or commercial brand site. Keep the implementation transparent and easy to edit.

## Scope and structure
- Static HTML and CSS only; no framework, database, build step, or external dependency.
- Pages: Home, Now, Notes, Things, Links, and About, with identical navigation and an accessible current-page state.
- Use relative paths so the site works at both a custom domain and a GitHub Pages project URL.
- Keep personal writing, works, links, and identity as prompts or honest empty states; do not invent user details.
- Add a README for preview, GitHub Pages publishing, and content editing. Ignore only OS/editor debris and generated output.

## Work sequence
1. Preserve the existing `.DS_Store`, initialize Git, and record this plan.
2. Add shared page styling and the six static pages.
3. Add publishing/editing guidance, then review navigation, paths, page structure, Git status, and diff.
4. Commit the complete v0.1 if changes can be safely isolated.

## Verification
- Inspect every page for consistent navigation, correct relative links, semantic landmarks, page title, and current-page indication.
- Check responsive CSS and static asset references.
- Run `git status` and `git diff --check`, review the diff, and record the commit hash.
- No automated test suite or build is needed for this dependency-free static site.

## Risks and rollback
- Avoid overwriting existing user files; only add site files and preserve `.DS_Store`.
- Keep all content local and static. No credentials, analytics, or external libraries.
- Revert the v0.1 commit to return to the original empty directory state; `.DS_Store` remains untouched.

## Delivery
Provide a working local static site, README, Git commit, preview command, and a short list of the first pages the user can fill in.
