from sentence_transformers import SentenceTransformer
from config.settings import settings

# Load once at startup
_model = SentenceTransformer(settings.EMBEDDING_MODEL)


def embed_text(text: str) -> list:
    """
    Returns a list[float] embedding suitable for MongoDB vector storage.
    """
    if not text or not text.strip():
        return []

    vec = _model.encode(text)
    return vec.tolist()


def embed_form_summary(schema: dict) -> list:
    """
    Create a compact text summary from a form schema and embed it.
    Useful for semantic retrieval.
    """
    fields = []

    if "fields" in schema:
        for f in schema["fields"]:
            label = f.get("label", "")
            ftype = f.get("type", "")
            fields.append(f"{label}:{ftype}")

    summary_text = " | ".join(fields)
    return embed_text(summary_text)
