import axios from "axios";

export async function getFormById(formId: string) {
  const res = await axios.get(`http://localhost:8000/forms/${formId}`);
  return res.data.form; // returns { schema, summary, ... }
}
