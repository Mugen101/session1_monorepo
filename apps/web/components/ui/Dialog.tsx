import React from "react";

export const Dialog = ({ open, children }: { open: boolean; children: React.ReactNode }) => (
  open ? <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
    <div className="bg-white dark:bg-muted rounded p-md shadow-lg">
      {children}
    </div>
  </div> : null
);
