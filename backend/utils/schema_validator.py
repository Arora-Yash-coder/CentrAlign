def validate_form_schema(schema: dict) -> bool:
    """
    Ensures minimum required keys exist in generated schema.
    Expected structure:
    {
       "title": "...",
       "fields": [
           { "label": "...", "type": "...", ... }
       ]
    }
    """

    if not isinstance(schema, dict):
        return False

    if "fields" not in schema:
        return False

    if not isinstance(schema["fields"], list):
        return False

    for field in schema["fields"]:
        if not isinstance(field, dict):
            return False

        if "label" not in field:
            return False

        if "type" not in field:
            return False

    return True
