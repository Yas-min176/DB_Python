from fastapi import FastAPI, Query, HTTPException, status, Depends
from fastapi_pagination import Page, pagination_params
from fastapi_pagination.ext.sqlalchemy import paginate
from sqlalchemy.exc import IntegrityError
from pydantic import BaseModel
from typing import List

# SQLAlchemy setup
# from sqlalchemy import create_engine, Column, String, Integer
# from sqlalchemy.orm import sessionmaker, declarative_base
# engine = create_engine('sqlite:///./example.db', echo=True)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()

app = FastAPI()

# SQLAlchemy model 
# class Atleta(Base):
#     __tablename__ = 'atletas'
#     id = Column(Integer, primary_key=True, index=True)
#     nome = Column(String, index=True)
#     cpf = Column(String, unique=True, index=True)
#     centro_treinamento = Column(String)
#     categoria = Column(String)

class Atleta(BaseModel):
    nome: str
    centro_treinamento: str
    categoria: str

@app.get("/atletas/", response_model=List[Atleta])
async def get_atletas(nome: str = Query(None, description="Filtrar por nome do atleta"),
                    cpf: str = Query(None, description="Filtrar por CPF do atleta")):
    # Replace with actual SQLAlchemy logic to query based on nome and cpf
    # Example: atletas = db.query(Atleta).filter_by(nome=nome, cpf=cpf).all()
    atletas = [
        {"nome": "Atleta 1", "centro_treinamento": "Centro 1", "categoria": "Categoria A"},
        {"nome": "Atleta 2", "centro_treinamento": "Centro 2", "categoria": "Categoria B"}
    ]
    return atletas

# Example endpoint for getting all atletas with response customization and pagination
@app.get("/atletas/all", response_model=Page[Atleta])
async def get_all_atletas(params: pagination_params = Depends()):
    # Replace with actual SQLAlchemy logic to fetch all atletas
    # Example: atletas = db.query(Atleta).all()
    atletas = [
        {"nome": "Atleta 1", "centro_treinamento": "Centro 1", "categoria": "Categoria A"},
        {"nome": "Atleta 2", "centro_treinamento": "Centro 2", "categoria": "Categoria B"}
    ]
    return paginate(atletas)

# Example exception handler for IntegrityError
@app.exception_handler(IntegrityError)
async def integrity_error_handler(request, exc):
    return HTTPException(status_code=status.HTTP_303_SEE_OTHER, 
                        detail=f"Já existe um atleta cadastrado com o cpf: {exc.params.get('cpf')}")

# Example SQLAlchemy setup and session management (if needed)
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
