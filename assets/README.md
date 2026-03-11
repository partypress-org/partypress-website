# Party Press website assets

## Logo variants

- **partypress-horizontal-org-transparent.png** — Horizontal, transparent background. Used in the **header** on all pages.
- **partypress-stacked-org-transparent.png** — Stacked, transparent background. Used in **hero/content** (e.g. homepage under the title).
- **partypress-horizontal-org.png** / **partypress-stacked-org.png** — Opaque background versions (kept for reference).
- **partypress-square.png** — Square (icon only). Source for favicons and app icons; favicon sizes are generated from this so they are not stretched.
- **partypress-logo.png** — Legacy full logo (symbol + "partypress"); kept for reference.

## Favicons

Generated from **partypress-square.png** (1:1) so they display without stretching:

- favicon-16x16.png, favicon-32x32.png, favicon-48x48.png
- favicon-180x180.png (Apple touch), favicon-192x192.png, favicon-512.png (PWA)

To regenerate: resize partypress-square.png to each size (e.g. with `sips -z 32 32 partypress-square.png --out favicon-32x32.png` on macOS).

## site.webmanifest

Web app manifest; references favicon-192x192.png and favicon-512.png.
