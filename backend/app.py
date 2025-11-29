from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.auth import router as auth_router
from routes.forms import router as forms_router
from routes.memory import router as memory_router
from routes.submissions import router as submissions_router
from routes.upload import router as upload_router

app = FastAPI(
    title="CentrAlignAI Backend",
    version="1.0.0",
    description="AI-powered dynamic form generator with context-aware memory."
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ROUTERS
app.include_router(auth_router, prefix="/auth", tags=["Authentication"])
app.include_router(forms_router, prefix="/forms", tags=["Forms"])
app.include_router(memory_router, prefix="/memory", tags=["Memory Retrieval"])
app.include_router(submissions_router, prefix="/submissions", tags=["Submissions"])
app.include_router(upload_router, prefix="/upload", tags=["Uploads"])

@app.get("/")
def root():
    return {"status": "ok", "message": "CentrAlignAI Backend Running"}
