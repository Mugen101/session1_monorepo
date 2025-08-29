"use client";
import React, { useState } from "react";
import { useSession } from "@/lib/session";
import { useRouter } from "next/navigation";

export default function SignInPage() {
  const [email, setEmail] = useState("");
  const { signIn } = useSession();
  const router = useRouter();

  const handleContinue = (e: React.FormEvent) => {
    e.preventDefault();
    signIn({ name: "Demo User" });
    router.push("/?mock=1");
  };

  return (
    <div className="max-w-md mx-auto mt-lg p-md bg-white rounded shadow">
      <h2 className="text-lg font-bold mb-md">Sign In</h2>
      <form onSubmit={handleContinue}>
        <label htmlFor="email" className="block mb-xs">
          Email
        </label>
        <input
          id="email"
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          className="w-full px-sm py-xs rounded border border-muted mb-md"
          required
        />
        <button
          type="submit"
          className="px-sm py-xs rounded bg-primary text-white w-full"
        >
          Continue
        </button>
      </form>
    </div>
  );
}
