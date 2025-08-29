# Design Tokens

This project uses a set of design tokens for consistent theming and UI design.

## Colors
- **primary:** Main brand color
- **muted:** Subtle backgrounds and borders
- **accent:** Highlights and call-to-action

## Spacing
- **xs, sm, md, lg:** Used for margins, paddings, and layout gaps

## Font Sizes
- **base, lg:** For body and headings

## Radii
- **radius:** For rounded corners on UI elements

## Dark Mode
- Uses the `class` strategy. The `.dark` class on `<html>` switches to dark theme tokens.

Tokens are defined in `global.css` and referenced in `tailwind.config.ts` for easy updates and consistent usage across components.
