import { describe, it, expect } from 'vitest';
import { render, screen } from '@testing-library/react';
import { Button } from '../Button';
import { Navbar } from '../Navbar';
import { ThemeToggle } from '../ThemeToggle';

describe('Button', () => {
  it('renders with text', () => {
    render(<Button>Click me</Button>);
    expect(screen.getByText('Click me')).toBeDefined();
  });
});

describe('Navbar', () => {
  it('renders without auth', () => {
    jest.mock('@/lib/session', () => ({ useSession: () => ({ user: null, status: 'unauthenticated', signOut: jest.fn() }) }));
    const { asFragment } = render(<Navbar />);
    expect(asFragment()).toMatchSnapshot();
  });
  it('renders with auth', () => {
    jest.mock('@/lib/session', () => ({ useSession: () => ({ user: { name: 'Test User' }, status: 'authenticated', signOut: jest.fn() }) }));
    const { asFragment } = render(<Navbar />);
    expect(asFragment()).toMatchSnapshot();
  });
});

describe('ThemeToggle', () => {
  it('renders and toggles', () => {
    render(<ThemeToggle />);
    expect(screen.getByRole('button')).toBeDefined();
  });
});
