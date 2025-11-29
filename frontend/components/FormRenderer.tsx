"use client";

import { useState } from "react";
import ImageUploader from "./ImageUploader";

export default function FormRenderer({
  schema,
  onChange,
}: {
  schema: any;
  onChange: (values: any) => void;
}) {
  const [values, setValues] = useState<any>({});

  const update = (label: string, value: any) => {
    const updated = { ...values, [label]: value };
    setValues(updated);
    onChange(updated);
  };

  return (
    <div className="flex flex-col gap-4">
      {schema?.fields?.map((field: any, i: number) => {
        const type = field.type;
        const label = field.label;

        return (
          <div key={i} className="flex flex-col gap-1">
            <label className="font-medium">{label}</label>

            {type === "text" && (
              <input
                className="border p-2 rounded-md"
                value={values[label] || ""}
                onChange={(e) => update(label, e.target.value)}
              />
            )}

            {type === "email" && (
              <input
                type="email"
                className="border p-2 rounded-md"
                value={values[label] || ""}
                onChange={(e) => update(label, e.target.value)}
              />
            )}

            {type === "number" && (
              <input
                type="number"
                className="border p-2 rounded-md"
                value={values[label] || ""}
                onChange={(e) => update(label, e.target.value)}
              />
            )}

            {type === "image" && (
              <ImageUploader onUploaded={(url) => update(label, url)} />
            )}
          </div>
        );
      })}
    </div>
  );
}
