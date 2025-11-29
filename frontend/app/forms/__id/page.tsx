"use client";

import { useEffect, useState } from "react";
import { useParams } from "next/navigation";
import Link from "next/link";
import axios from "axios";

export default function FormPreviewPage() {
  const { __id } = useParams(); // folder name '__id'
  const [form, setForm] = useState<any>(null);

  useEffect(() => {
    if (!__id) return;

    axios
      .get(`http://localhost:8000/forms/${__id}`)
      .then((res) => setForm(res.data.form))
      .catch(() => {});
  }, [__id]);

  if (!form)
    return (
      <main className="p-6">
        <div className="text-gray-600">Loading...</div>
      </main>
    );

  return (
    <main className="p-6">
      <h1 className="text-2xl font-semibold mb-3">
        Form Preview
      </h1>

      <div className="p-4 bg-white rounded-md shadow">
        <h2 className="font-medium mb-2">{form.summary}</h2>

        <div className="flex flex-col gap-2">
          {form.schema.fields?.map((field: any, idx: number) => (
            <div
              key={idx}
              className="p-3 border rounded-md bg-gray-50 text-sm"
            >
              <strong>{field.label}</strong> — <em>{field.type}</em>
            </div>
          ))}
        </div>

        <Link
          href={`/forms/${__id}/submit`}
          className="inline-block mt-4 px-4 py-2 bg-blue-600 text-white rounded-md"
        >
          Open Live Form
        </Link>
      </div>
    </main>
  );
}
