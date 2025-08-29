# UI Review Checklist

## Accessibility
- [ ] Keyboard focus is visible and clear on all interactive elements
- [ ] "Skip to content" link is present and works
- [ ] All images have descriptive alt text
- [ ] Sufficient color contrast for text and UI elements
- [ ] No keyboard traps; all navigation is possible via keyboard
- [ ] ARIA roles and labels are used appropriately
- [ ] No redundant roles or labels
- [ ] Forms have associated labels
- [ ] No positive tabindex except for intended focus order

## Usability
- [ ] Navigation is intuitive and consistent
- [ ] Sidebar and Navbar are accessible and responsive
- [ ] Theme toggle works and is accessible
- [ ] UI primitives (Button, Card, Dialog, Input) are usable and accessible

## Visual Design
- [ ] Font sizes and spacing are consistent
- [ ] Responsive layout on all screen sizes
- [ ] Design tokens (colors, radius, spacing) are applied
- [ ] Dark mode and light mode are visually balanced

## Testing
- [ ] All unit tests pass
- [ ] Storybook stories are available for all UI components
- [ ] Accessibility lint passes (eslint-plugin-jsx-a11y)

---
_Last updated: August 26, 2025_
