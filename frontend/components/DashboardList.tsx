"use client";

import Link from "next/link";

export default function DashboardList({ forms }: { forms: any[] }) {
  if (!forms || forms.length === 0)
    return <div className="text-gray-600">No forms yet.</div>;

  return (
    <div className="flex flex-col gap-4">
      {forms.map((form: any) => (
        <Link
          key={form.id}
          href={`/forms/${form.id}`}
          className="p-4 bg-white rounded-md shadow hover:bg-gray-50"
        >
          <div className="font-medium">{form.summary}</div>

          <div className="text-sm text-gray-500">
            {new Date(form.created_at).toLocaleString()}
          </div>
        </Link>
      ))}
    </div>
  );
}
