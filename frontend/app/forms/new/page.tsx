"use client";

import { useState } from "react";
import axios from "axios";

export default function NewFormPage() {
  const [prompt, setPrompt] = useState("");
  const [schema, setSchema] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const generateForm = async () => {
    setLoading(true);
    setSchema(null);

    const token = localStorage.getItem("token");
    if (!token) {
      alert("Login required");
      setLoading(false);
      return;
    }

    try {
      const res = await axios.post(
        "http://localhost:8000/forms/generate",
        { prompt },
        { headers: { Authorization: `Bearer ${token}` } }
      );

      setSchema(res.data.schema);
    } catch (e) {
      alert("Error generating form");
    }

    setLoading(false);
  };

  return (
    <main className="p-6">
      <h1 className="text-2xl font-semibold mb-4">Create New Form</h1>

      <textarea
        className="w-full p-3 border rounded-md mb-4"
        rows={4}
        placeholder="Describe the form you want..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />

      <button
        onClick={generateForm}
        className="px-4 py-2 bg-blue-600 text-white rounded-md"
      >
        {loading ? "Generating..." : "Generate"}
      </button>

      {schema && (
        <div className="mt-6 p-4 bg-white shadow rounded-md">
          <h2 className="text-lg font-semibold mb-2">Generated Schema:</h2>
          <pre className="bg-gray-100 p-3 rounded-md text-sm overflow-auto">
            {JSON.stringify(schema, null, 2)}
          </pre>
        </div>
      )}
    </main>
  );
}
