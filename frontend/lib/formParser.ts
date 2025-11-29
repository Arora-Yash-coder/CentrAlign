export function parseFormSchema(schema: any) {
  if (!schema || !schema.fields) return [];

  return schema.fields.map((field: any) => {
    return {
      label: field.label || "",
      type: field.type || "text",
      required: field.required ?? false,
      placeholder: field.placeholder || "",
      options: field.options || [],
    };
  });
}
