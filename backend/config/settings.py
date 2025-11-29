from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # APP
    APP_NAME: str = "CentrAlignAI Backend"
    APP_VERSION: str = "1.0.0"

    # DATABASE
    MONGODB_URI: str
    MONGODB_DB_NAME: str = "centralign_ai"

    # AUTH
    JWT_SECRET: str
    JWT_ALGORITHM: str = "HS256"
    JWT_EXPIRY_HOURS: int = 24

    # CLOUDINARY
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str

    # AI PROVIDER
    AI_API_KEY: str
    AI_MODEL: str = "gemini-1.5-flash"

    # EMBEDDINGS MODEL (local or remote)
    EMBEDDING_MODEL: str = "all-MiniLM-L6-v2"

    class Config:
        env_file = ".env"
        case_sensitive = True


settings = Settings()
