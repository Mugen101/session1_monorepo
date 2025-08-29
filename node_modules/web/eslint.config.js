import js from '@eslint/js';
import jsxA11y from 'eslint-plugin-jsx-a11y';
import nextPlugin from 'eslint-plugin-next';

export default [
  js.configs.recommended,
  {
    plugins: {
      'jsx-a11y': jsxA11y,
      'next': nextPlugin,
    },
    rules: {
      'jsx-a11y/anchor-is-valid': 'warn',
      'jsx-a11y/no-static-element-interactions': 'warn',
      'jsx-a11y/tabindex-no-positive': 'warn',
      'jsx-a11y/no-autofocus': 'warn',
      'jsx-a11y/no-noninteractive-element-interactions': 'warn',
      'jsx-a11y/no-noninteractive-tabindex': 'warn',
      'jsx-a11y/click-events-have-key-events': 'warn',
      'jsx-a11y/no-redundant-roles': 'warn',
      'jsx-a11y/label-has-associated-control': 'warn',
      'jsx-a11y/control-has-associated-label': 'warn',
      // Next.js recommended rules
      'next/no-html-link-for-pages': 'off',
      'next/no-head-element': 'off',
    },
  },
];
