from fastapi import FastAPI
from typing import List, Any
from contextlib import asynccontextmanager
import dill
from pydantic import BaseModel

def custom_load(path):
    with open(path, 'rb') as f:
        return dill.load(f)
    
class Product(BaseModel):
    product_id: str
    product_name: str

@asynccontextmanager
async def lifespan(app: FastAPI):
    global sistema_carregado
    # Carrega o modelo na inicialização
    sistema_carregado = custom_load('/app/sistema_recomendacao_endpoint/sist_recomendacao.pkl')
    yield
    # Aqui poderia ser colocado o código de cleanup, se necessário

# Instancia a aplicação com lifespan configurado
app = FastAPI(lifespan=lifespan)

@app.get("/recomenda_produtos", response_model=List[Any])
async def recomenda_produtos(product_id: str):
    """
    Retorna os produtos recomendados.
    """
    return sistema_carregado.recomendar(product_id)

@app.get("/get_products_ids", response_model=List[Product])
async def get_products_ids():
    """
    Retorna a lista de IDs dos produtos.
    """
    return [{"product_id": p[0], "product_name": p[1]} for p in sistema_carregado.listar_produtos()]
