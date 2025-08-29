import React from "react";
import type { Metadata } from 'next';
import './globals.css';
import { AppShell } from '@/components/ui/AppShell';
import { ThemeToggle } from '@/components/ui/ThemeToggle';
import { SessionProvider } from '@/lib/session';

export const metadata: Metadata = {
  title: 'TravelG3n',
  description: 'Next.js monorepo foundation',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body suppressHydrationWarning={true}>
        {/* Top bar with skip link and theme toggle side by side */}
        <div className="flex items-center gap-4 absolute left-2 top-2 z-50">
          <a
            href="#main-content"
            className="bg-white dark:bg-black text-primary px-4 py-2 rounded focus:outline-none focus-visible:ring-2 focus-visible:ring-accent transition-transform -translate-y-16 focus:translate-y-0"
          >
            Skip to content
          </a>
          <ThemeToggle />
        </div>
        <SessionProvider>
          <AppShell>
            <main id="main-content">
              {children}
            </main>
          </AppShell>
        </SessionProvider>
      </body>
    </html>
  );
}
