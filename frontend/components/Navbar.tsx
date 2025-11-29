"use client";

import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full bg-white shadow px-6 py-3 flex justify-between items-center">
      <Link href="/" className="font-semibold text-lg">
        CentrAlignAI
      </Link>

      <div className="flex gap-4">
        <Link href="/dashboard" className="text-gray-700 hover:text-black">
          Dashboard
        </Link>

        <Link href="/forms/new" className="text-gray-700 hover:text-black">
          New Form
        </Link>
      </div>
    </nav>
  );
}
