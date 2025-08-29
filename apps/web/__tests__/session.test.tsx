import { renderHook, act } from '@testing-library/react';
import { SessionProvider, useSession } from '@/lib/session';

describe('useSession', () => {
  it('returns unauthenticated by default', () => {
    const { result } = renderHook(() => useSession(), {
      wrapper: SessionProvider,
    });
    expect(result.current.status).toBe('unauthenticated');
    expect(result.current.user).toBeNull();
  });

  it('returns authenticated when mock=1', () => {
    window.history.pushState({}, '', '/?mock=1');
    const { result } = renderHook(() => useSession(), {
      wrapper: SessionProvider,
    });
    expect(result.current.status).toBe('authenticated');
    expect(result.current.user?.name).toBe('Demo User');
  });
});
