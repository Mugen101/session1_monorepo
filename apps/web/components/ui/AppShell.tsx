import React from "react";
import { Navbar } from "@/components/ui/Navbar";
import { Sidebar } from "@/components/ui/Sidebar";

export const AppShell = ({ children }: { children: React.ReactNode }) => (
  <div className="flex h-screen">
    <Sidebar />
    <div className="flex-1 flex flex-col">
      <Navbar />
      <main className="p-md flex-1 bg-white dark:bg-muted">{children}</main>
    </div>
  </div>
);
