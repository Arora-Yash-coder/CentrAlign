from config.db_config import get_db
from services.embedding_service import embed_text

K = 5  # top-K relevant forms to retrieve


def retrieve_relevant_forms(prompt: str, user_id: str):
    """
    1. Embed the incoming prompt.
    2. Query MongoDB vector index for nearest summaries.
    3. Return trimmed context (only purpose + fields).
    """

    db = get_db()
    embedding = embed_text(prompt)

    if not embedding:
        return []

    pipeline = [
        {
            "$search": {
                "index": "form_vector_index",
                "knnBeta": {
                    "vector": embedding,
                    "path": "embedding",
                    "k": K
                }
            }
        },
        {"$match": {"user_id": user_id}},
        {"$limit": K},
        {
            "$project": {
                "_id": 1,
                "summary": 1,
                "schema.fields.label": 1,
                "schema.fields.type": 1
            }
        }
    ]

    results = list(db.forms.aggregate(pipeline))

    # Trim into context required by AI prompt
    context = []
    for r in results:
        fields = []
        for f in r.get("schema", {}).get("fields", []):
            fields.append({
                "label": f.get("label"),
                "type": f.get("type")
            })

        context.append({
            "summary": r.get("summary", ""),
            "fields": fields
        })

    return context
