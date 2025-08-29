"use client";
import React, { createContext, useContext, useState, useEffect } from "react";

interface User {
  name: string;
}

interface Session {
  user: User | null;
  status: "authenticated" | "unauthenticated";
}

const SessionContext = createContext<{
  session: Session;
  signIn: (user: User) => void;
  signOut: () => void;
}>({
  session: { user: null, status: "unauthenticated" },
  signIn: () => {},
  signOut: () => {},
});

export const SessionProvider = ({ children }: { children: React.ReactNode }) => {
  const [session, setSession] = useState<Session>({ user: null, status: "unauthenticated" });

  useEffect(() => {
    const params = new URLSearchParams(window.location.search);
    if (params.get("mock") === "1") {
      setSession({ user: { name: "Demo User" }, status: "authenticated" });
    }
  }, []);

  const signIn = (user: User) => {
    setSession({ user, status: "authenticated" });
    window.location.search = "?mock=1";
  };

  const signOut = () => {
    setSession({ user: null, status: "unauthenticated" });
    window.location.search = "";
  };

  return (
    <SessionContext.Provider value={{ session, signIn, signOut }}>
      {children}
    </SessionContext.Provider>
  );
};

export const useSession = () => {
  const { session, signIn, signOut } = useContext(SessionContext);
  return { ...session, signIn, signOut };
};
