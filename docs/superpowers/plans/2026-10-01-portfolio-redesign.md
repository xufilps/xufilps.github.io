# Personal Portfolio Redesign Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** Replace the current personal-corner pages with an editable four-page portfolio shell.

**Architecture:** Keep real content in semantic static HTML and share styling through `styles.css`. Use `theme.js` only for the optional theme toggle; navigation and content must work without it.

**Tech Stack:** HTML5, CSS, vanilla JavaScript, GitHub Pages.

## Global Constraints

- Do not invent personal biography, project outcomes, writing, images, or contact details.
- No framework, build step, remote assets, or analytics.
- Do not stage the pre-existing deletion of `docs/project-plan.md`.
- Keep the existing Markdown note in Git but out of the new site's navigation.

---

### Task 1: Shared shell and visual system

**Files:** Modify `styles.css`; create `theme.js`; modify `index.html`.

**Interfaces:** The theme button uses `data-theme-toggle` and `aria-pressed`; `theme.js` writes `data-theme` on the root element. All pages link to the same shared files with correct relative paths.

- [x] Write the homepage with `<header>`, `<nav>`, `<main>`, sections, `<aside>`, and `<footer>`; keep skip navigation and a single `<h1>`.
- [x] Add the editorial layout, responsive breakpoints, light and dark color tokens, visible focus styles, and reduced motion rules to `styles.css`.
- [x] Implement theme preference loading and button behavior in `theme.js`, guarded when storage is unavailable.
- [x] Check the homepage at desktop and mobile widths, including keyboard focus and no-script navigation.

### Task 2: Portfolio destinations

**Files:** Create `projects/index.html`, `writing/index.html`; modify `about/index.html`; remove obsolete HTML pages under `now`, `notes`, `things`, and `links`.

**Interfaces:** Navigation destinations are `./`, `projects/`, `writing/`, and `about/` from the root; inner pages use `../` prefixes. Each page sets its own `aria-current="page"`.

- [x] Add the project destination with an empty state and a documented entry structure for future real work.
- [x] Add the writing destination with an empty state and a documented list structure for future published articles.
- [x] Rewrite About with clear empty spaces for biography, practice, and contact methods.
- [x] Remove old HTML destinations while retaining `notes/notes-20260930.md` in Git.
- [x] Check every internal link and confirm each page has a title, description, landmarks, and a single `<h1>`.

### Task 3: Handoff and verification

**Files:** Modify `README.md`; modify this plan's checkboxes when tasks are complete.

**Interfaces:** `README.md` explains local preview, where to edit real content, GitHub Pages publication, and the intentionally empty areas.

- [x] Preview all four routes and the theme control in a browser, including a narrow viewport.
- [x] Run `git diff --check`, inspect staged paths, and confirm `docs/project-plan.md` is unstaged.
- [x] Commit redesign files on `feat/portfolio-redesign-20261001` with a clear message.

## Risk and rollback

The prior site is recoverable from branch history. The existing Markdown note is retained. Reverting the redesign commit restores the previous site files; the unrelated working-tree deletion remains separate.
