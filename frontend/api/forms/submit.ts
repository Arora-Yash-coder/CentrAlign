import axios from "axios";

export async function submitForm(formId: string, data: any) {
  const res = await axios.post(
    `http://localhost:8000/submissions/${formId}`,
    data
  );

  return res.data; // simple success message
}
