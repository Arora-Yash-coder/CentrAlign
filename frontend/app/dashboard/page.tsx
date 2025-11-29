"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import axios from "axios";

export default function DashboardPage() {
  const [forms, setForms] = useState([]);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) return;

    axios
      .get("http://localhost:8000/forms", {
        headers: { Authorization: `Bearer ${token}` },
      })
      .then((res) => setForms(res.data.forms || []))
      .catch(() => {});
  }, []);

  return (
    <main className="p-6">
      <h1 className="text-2xl font-semibold mb-4">Your Forms</h1>

      <div className="flex flex-col gap-4">
        {forms.length === 0 && (
          <div className="text-gray-600">No forms created yet.</div>
        )}

        {forms.map((form: any) => (
          <Link
            key={form.id}
            href={`/forms/${form.id}`}
            className="p-4 bg-white shadow rounded-md hover:bg-gray-50"
          >
            <div className="font-medium">{form.summary}</div>
            <div className="text-sm text-gray-500">
              {new Date(form.created_at).toLocaleString()}
            </div>
          </Link>
        ))}
      </div>
    </main>
  );
}
