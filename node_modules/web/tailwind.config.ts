import type { Config } from 'tailwindcss';

const config: Config = {
  darkMode: 'class',
  content: [
    './app/**/*.{ts,tsx,js,jsx}',
    './components/**/*.{ts,tsx,js,jsx}'
  ],
  theme: {
    extend: {
      colors: {
        primary: 'var(--color-primary)',
        muted: 'var(--color-muted)',
        accent: 'var(--color-accent)'
      },
      spacing: {
        xs: 'var(--spacing-xs)',
        sm: 'var(--spacing-sm)',
        md: 'var(--spacing-md)',
        lg: 'var(--spacing-lg)'
      },
      fontSize: {
        base: 'var(--font-size-base)',
        lg: 'var(--font-size-lg)'
      },
      borderRadius: {
        DEFAULT: 'var(--radius)'
      }
    }
  },
  plugins: []
};

export default config;
