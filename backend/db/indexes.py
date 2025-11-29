from .client import get_db


def create_indexes():
    db = get_db()

    # USERS -------------------------------------------------------
    db.users.create_index("email", unique=True)

    # FORMS -------------------------------------------------------
    db.forms.create_index("user_id")
    db.forms.create_index("created_at")

    """
    IMPORTANT:
    MongoDB Atlas Search vector index must be created in the Atlas UI.

    Name required in code: "form_vector_index"
    Path: embedding (array of floats)
    -----------------------------------------
    JSON example to create in Atlas:

    {
      "fields": [
        {
          "type": "knnVector",
          "path": "embedding",
          "numDimensions": 384,
          "similarity": "cosine"
        }
      ]
    }
    """

    # SUBMISSIONS -------------------------------------------------
    db.submissions.create_index("form_id")
    db.submissions.create_index("submitted_at")

    return True
