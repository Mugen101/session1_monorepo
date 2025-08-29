import React from 'react';

export function Sidebar() {
  return (
    <aside className="w-64 h-full bg-muted p-md flex flex-col gap-md shadow">
      <nav>
        <ul className="space-y-sm">
          <li><a href="/" className="text-lg">Home</a></li>
          <li><a href="/about" className="text-lg">About</a></li>
          <li><a href="/auth/sign-in" className="text-lg">Sign In</a></li>
        </ul>
      </nav>
    </aside>
  );
}
