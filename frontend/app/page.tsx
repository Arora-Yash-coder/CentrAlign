"use client";

import Link from "next/link";

export default function HomePage() {
  return (
    <main className="flex flex-col items-center justify-center h-screen gap-6">
      <h1 className="text-3xl font-semibold">CentrAlignAI</h1>
      <p className="text-gray-600">AI-powered dynamic form generator</p>

      <div className="flex gap-4">
        <Link
          href="/dashboard"
          className="px-4 py-2 bg-blue-600 text-white rounded-md"
        >
          Go to Dashboard
        </Link>

        <Link
          href="/forms/new"
          className="px-4 py-2 bg-gray-800 text-white rounded-md"
        >
          Create New Form
        </Link>
      </div>
    </main>
  );
}
