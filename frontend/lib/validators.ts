export function validateEmail(email: string) {
  const re = /\S+@\S+\.\S+/;
  return re.test(email);
}

export function validateRequired(value: any) {
  return value !== null && value !== undefined && value !== "";
}

export function validateNumber(value: any) {
  return !isNaN(Number(value));
}
