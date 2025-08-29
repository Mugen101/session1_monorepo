import '@testing-library/jest-dom';
import React from 'react';
jest.mock('next/navigation', () => ({
  useRouter: () => ({
    push: jest.fn(),
  }),
}));
import { render, screen, fireEvent } from '@testing-library/react';
import { Navbar } from '@/components/ui/Navbar';
import { SessionProvider } from '@/lib/session';

describe('Navbar', () => {
  it('shows Sign in when unauthenticated', () => {
    render(
      <SessionProvider>
        <Navbar />
      </SessionProvider>
    );
    expect(screen.getByText('Sign in')).toBeInTheDocument();
  });

  it('shows avatar and Sign out when authenticated', () => {
    window.history.pushState({}, '', '/?mock=1');
    render(
      <SessionProvider>
        <Navbar />
      </SessionProvider>
    );
    expect(screen.getByText('Demo User')).toBeInTheDocument();
    expect(screen.getByText('Sign out')).toBeInTheDocument();
  });
});
