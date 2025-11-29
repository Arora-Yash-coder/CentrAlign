"use client";

import { useState, useEffect } from "react";
import { useParams } from "next/navigation";
import axios from "axios";

export default function LiveFormPage() {
  const { __id } = useParams();
  const [form, setForm] = useState<any>(null);
  const [values, setValues] = useState<any>({});
  const [submitting, setSubmitting] = useState(false);

  useEffect(() => {
    if (!__id) return;

    axios
      .get(`http://localhost:8000/forms/${__id}`)
      .then((res) => setForm(res.data.form))
      .catch(() => {});
  }, [__id]);

  const updateValue = (label: string, value: any) => {
    setValues((v: any) => ({ ...v, [label]: value }));
  };

  const uploadImage = async (file: File, label: string) => {
    const formData = new FormData();
    formData.append("file", file);

    const res = await axios.post("http://localhost:8000/upload/image", formData, {
      headers: { "Content-Type": "multipart/form-data" },
    });

    updateValue(label, res.data.url);
  };

  const submit = async () => {
    setSubmitting(true);
    try {
      await axios.post(`http://localhost:8000/submissions/${__id}`, values);
      alert("Submitted successfully");
      setValues({});
    } catch (e) {
      alert("Submit failed");
    }
    setSubmitting(false);
  };

  if (!form)
    return (
      <main className="p-6">
        <div className="text-gray-600">Loading...</div>
      </main>
    );

  return (
    <main className="p-6">
      <h1 className="text-2xl font-semibold mb-3">{form.summary}</h1>

      <div className="flex flex-col gap-4 bg-white p-5 rounded-md shadow">
        {form.schema.fields?.map((field: any, i: number) => {
          const label = field.label;
          const type = field.type;

          return (
            <div key={i} className="flex flex-col gap-1">
              <label className="font-medium">{label}</label>

              {type === "text" && (
                <input
                  className="border p-2 rounded-md"
                  value={values[label] || ""}
                  onChange={(e) => updateValue(label, e.target.value)}
                />
              )}

              {type === "email" && (
                <input
                  type="email"
                  className="border p-2 rounded-md"
                  value={values[label] || ""}
                  onChange={(e) => updateValue(label, e.target.value)}
                />
              )}

              {type === "number" && (
                <input
                  type="number"
                  className="border p-2 rounded-md"
                  value={values[label] || ""}
                  onChange={(e) => updateValue(label, e.target.value)}
                />
              )}

              {type === "image" && (
                <input
                  type="file"
                  accept="image/*"
                  className="border p-2 rounded-md"
                  onChange={(e) =>
                    e.target.files && uploadImage(e.target.files[0], label)
                  }
                />
              )}
            </div>
          );
        })}

        <button
          onClick={submit}
          className="px-4 py-2 bg-blue-600 text-white rounded-md"
        >
          {submitting ? "Submitting..." : "Submit"}
        </button>
      </div>
    </main>
  );
}
