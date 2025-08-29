"use client";
import React from 'react';
import { PageHeader } from './PageHeader';
import { useSession } from '@/lib/session';
import { useRouter } from 'next/navigation';

export function Navbar() {
  const { user, status, signOut } = useSession();
  const router = useRouter();

  return (
    <nav className="flex items-center justify-between px-md py-xs bg-primary text-white">
      <PageHeader title="TravelG3n" />
      <div>
        {status === 'authenticated' ? (
          <>
            <span className="inline-flex items-center mr-sm">
              <img src="https://ui-avatars.com/api/?name=Demo+User" alt="avatar" className="w-6 h-6 rounded-full mr-xs" />
              {user?.name}
            </span>
            <button
              className="px-sm py-xs rounded bg-accent text-white"
              onClick={() => { signOut(); router.push('/'); }}
            >
              Sign out
            </button>
          </>
        ) : (
          <button
            className="px-sm py-xs rounded bg-accent text-white"
            onClick={() => router.push('/auth/sign-in')}
          >
            Sign in
          </button>
        )}
      </div>
    </nav>
  );
}
