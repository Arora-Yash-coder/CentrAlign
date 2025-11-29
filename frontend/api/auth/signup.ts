import axios from "axios";

export async function signupUser(email: string, password: string) {
  const res = await axios.post("http://localhost:8000/auth/signup", {
    email,
    password,
  });

  return res.data; // success message
}
