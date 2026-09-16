# AGENT.md — Project Router

Read this file first, before any other action, on every task. It tells you
which project/stack you're in and which skill files to load before writing or
changing anything. Never fall back to general framework knowledge when a
matching skill file exists — the skill file wins.

## Step 1 — Detect the stack
Look at the project root for these markers, in order, and stop at the first
match:

| Stack | Marker files | rules folder |
|---|---|---|
| Flask SSR (Python) | `app.py` **and** `templates/` **and** `static/`, or `requirements.txt` containing `flask` | `rules/flask-ssr/` |
` |
| *(add new stacks here as you create their skill folders)* | | |

If nothing matches, or two stacks could plausibly match, **ask which stack
this is** before doing any structural work (don't guess).

## Step 2 — Load that stack's rules
Read every numbered file in the matched folder, in order, before starting the
task. They're small on purpose — read all of them, not just the one that
sounds most relevant to the current request.

## Step 3 — Do the task using those conventions
Apply the loaded skill files' rules over any generic/training-data default,
including things like file layout, naming, and size limits. If a task needs a
convention not covered by any skill file, follow the closest existing pattern
in the project and flag the gap rather than inventing a new one silently.

---

## Stacks

### Flask SSR (Python)
**Trigger:** `app.py` + `templates/` + `static/`, or `flask` in
`requirements.txt`.

**rules (read all, in order):**
1. `rules/01-project-structure.md`
2. `rules/02-server-setup.md`
3. `rules/03-templating-jinja.md`
4. `rules/04-responsive-css.md`
5. `rules/05-performance-assets.md`
6. `rules/06-deployment-security.md`

**Quick-reference (full detail is in the files above — don't stop here):**
- Components → Jinja **macros** (`templates/macros.html`) or
  `templates/partials/`; component styles → one file per component under
  `static/css/components/`, imported into `style.css`.
- **120-line cap** on any single route file, template, macro file, or CSS
  file. Split (new blueprint / partial / smaller component) past that.
- CSRF token (Flask-WTF) required on every state-changing `<form>`.
- Never `app.run(debug=True)` in production; `waitress`/`gunicorn` behind a
  reverse proxy instead.
- Secrets in `.env`, loaded via `python-dotenv`, never hardcoded.

### MERN
**Trigger:** `package.json` with `react` + `express`/`mongoose`, `client/` +
`server/` folders present.

**rules:** not yet written — see `rules/mern/00-add-your-rules-here.md`
for the folder's expected shape. Once populated, list the files here the same
way as the Flask section above.

**Quick-reference (placeholder until the skill files exist):**
- Components → `client/src/components/`, one component per file.
- Component styles → `client/src/componentStyles/` (or a co-located
  `Component.module.css` next to the component — pick one and be consistent).
- **120-line cap** per component/route/controller file.

---

## Adding a new stack later
1. Create `rules/<stack-name>/` with numbered `.md` files, same style as
   `flask-ssr/` — one topic per file, short, example-driven.
2. Add a detection row to the table in Step 1.
3. Add a `### <Stack>` section here: trigger markers, the ordered file list,
   and a quick-reference summary.
4. Don't delete or rename existing stacks' folders — other projects may still
   point at them.

## Global rules (apply regardless of stack)
- Read this file and the matched skill folder before making any structural
  decision (folder layout, file naming, where new code goes).
- Never mix conventions from two stacks in the same project.
- If a project matches no known stack, ask before assuming a layout.
## Global rules (apply regardless of stack)
- Always use the Python interpreter path defined in `rules/env.md` for any
  Python command (running scripts, pip installs, tests, etc.). Do not fall
  back to the system `python` on PATH.
- Read this file and the matched skill folder before making any structural
  decision (folder layout, file naming, where new code goes).
- Never mix conventions from two stacks in the same project.
- If a project matches no known stack, ask before assuming a layout.