import axios from "axios";

export async function generateForm(prompt: string) {
  const token = typeof window !== "undefined" ? localStorage.getItem("token") : null;

  const res = await axios.post(
    "http://localhost:8000/forms/generate",
    { prompt },
    {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    }
  );

  return res.data; // contains { form_id, schema }
}
