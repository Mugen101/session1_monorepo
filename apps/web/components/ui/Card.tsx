import React from "react";

export const Card = ({ children }: { children: React.ReactNode }) => (
  <div className="rounded bg-muted p-md shadow">
    {children}
  </div>
);
