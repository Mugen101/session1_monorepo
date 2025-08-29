
"use client";
import React, { useCallback } from "react";

export const ThemeToggle = () => {
  const toggleTheme = useCallback(() => {
    const html = document.documentElement;
    html.classList.toggle("dark");
  }, []);

  return (
    <button className="px-sm py-xs rounded bg-accent text-white" onClick={toggleTheme}>
      Toggle Theme
    </button>
  );
};
