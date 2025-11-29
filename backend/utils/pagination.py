from typing import List, Any


def paginate(items: List[Any], page: int = 1, limit: int = 10):
    """
    Basic in-memory pagination helper.
    For DB queries, use skip/limit directly.
    """
    if page < 1:
        page = 1

    start = (page - 1) * limit
    end = start + limit

    return {
        "page": page,
        "limit": limit,
        "total": len(items),
        "results": items[start:end]
    }
