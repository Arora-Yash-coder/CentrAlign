"use client";

import { useState } from "react";
import axios from "axios";

export default function ImageUploader({
  onUploaded,
}: {
  onUploaded: (url: string) => void;
}) {
  const [uploading, setUploading] = useState(false);

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (!file) return;

    setUploading(true);

    try:
      const formData = new FormData();
      formData.append("file", file);

      const res = await axios.post(
        "http://localhost:8000/upload/image",
        formData,
        {
          headers: { "Content-Type": "multipart/form-data" },
        }
      );

      onUploaded(res.data.url);
    } catch (err) {
      alert("Image upload failed");
    }

    setUploading(false);
  };

  return (
    <div className="flex flex-col gap-2">
      <input
        type="file"
        accept="image/*"
        className="border p-2 rounded-md"
        onChange={handleUpload}
      />

      {uploading && (
        <span className="text-sm text-gray-600">Uploading...</span>
      )}
    </div>
  );
}
