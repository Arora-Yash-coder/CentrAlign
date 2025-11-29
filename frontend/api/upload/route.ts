import axios from "axios";

export async function uploadImage(file: File) {
  const formData = new FormData();
  formData.append("file", file);

  const res = await axios.post("http://localhost:8000/upload/image", formData, {
    headers: { "Content-Type": "multipart/form-data" },
  });

  return res.data.url; // secure Cloudinary URL
}
