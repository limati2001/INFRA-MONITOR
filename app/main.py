from fastapi import FastAPI
from app.core.database import engine, Base
from app.models import Service

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Monitor de Infraestrutura", version="0.1.0")

@app.get("/health")
def health_check():
    return {"status": "ok"}
