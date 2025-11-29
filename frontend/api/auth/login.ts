import axios from "axios";

export async function loginUser(email: string, password: string) {
  const res = await axios.post("http://localhost:8000/auth/login", {
    email,
    password,
  });

  return res.data; // contains { token, user_id }
}
