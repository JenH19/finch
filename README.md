# Bright Finch Coaching — new site

Static HTML/CSS site, "Fieldnotes" design direction (ivory paper, moss/rust
ink, Fraunces + Work Sans + IBM Plex Mono). No CMS, no build step, no
hosting fees — same pattern as the other sites.

## Folder structure

```
brightfinch/
├── index.html
├── offerings.html
├── about.html
├── contact.html
├── css/style.css
├── js/main.js
├── images/              ← populated by download_images.py
└── download_images.py
```

## 1. Get the real images

The image URLs point at the old Squarespace CDN, which can't be fetched
from a sandboxed environment — run this on your own machine, from inside
the `brightfinch/` folder:

```
python3 download_images.py
```

This pulls 7 images (hero, two event photos, headshot, three offering
photos) into `images/` with the filenames the HTML already expects.

## 2. Wire up the contact form

`contact.html` posts to a Formspree endpoint. Swap in the real form ID:

```html
<form class="contact-form" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
```

(Create a new Formspree form, or reuse a form ID if you want submissions
in the same inbox as the FalconRock site.)

## 3. Push to GitHub

```
git init
git add .
git commit -m "Rebuild Bright Finch Coaching as a static site"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

**Important:** upload/push the whole folder structure as-is — flattening
it breaks the `css/`, `js/`, and `images/` paths.

## 4. Turn on GitHub Pages

Repo → Settings → Pages → Deploy from branch → `main` / `root`.

## 5. Point Cloudflare at it

In Cloudflare DNS for brightfinchcoaching.com, point the A/CNAME records
at GitHub Pages (same pattern as the other sites):

- `A` records for the apex domain → GitHub Pages' 4 IPs
- `CNAME` for `www` → `<your-username>.github.io`

Add a `CNAME` file to the repo root containing `www.brightfinchcoaching.com`
(or the apex, whichever you're using as canonical) so GitHub Pages knows
the custom domain.

## 6. Cancel Squarespace

Once the new site is live and DNS has propagated, cancel the Squarespace
plan. Check the billing date first — annual plans generally don't refund
past the 14-day window.

## Editing later (via Claude Code)

Everything is plain HTML/CSS — no build step. Ask Claude Code to edit
copy, swap images, or add a new offering card directly in the relevant
`.html` file.
