# Party Press website assets

## Logo variants

- **partypress-horizontal-org-white.png** — Horizontal, plain white background. Used in the **header** on all pages.
- **partypress-stacked-org-white.png** — Stacked, plain white background. Used in **hero/content** (e.g. homepage under the title).
- **partypress-icon-white.png** — Square, icon only (no text), plain white background. Source for all favicons.
- **partypress-square.png** — Square icon (legacy). Favicons are now generated from partypress-icon-white.png.
- **partypress-logo.png** — Legacy full logo (symbol + "partypress"); kept for reference.

## Favicons

Generated from **partypress-icon-white.png** (icon only, white background, 1:1):

- favicon-16x16.png, favicon-32x32.png, favicon-48x48.png
- favicon-180x180.png (Apple touch), favicon-192x192.png, favicon-512.png (PWA)

To regenerate: resize partypress-icon-white.png to each size (e.g. with `sips -z 32 32 partypress-square.png --out favicon-32x32.png` on macOS).

## site.webmanifest

Web app manifest; references favicon-192x192.png and favicon-512.png.
