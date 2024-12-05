from fastapi import FastAPI
from typing import List, Any
from contextlib import asynccontextmanager
import dill
from pydantic import BaseModel

#esse daqui é para dar carga no modelo
def custom_load(path):
    with open(path, 'rb') as f:
        return dill.load(f)

#essa instanciação de classe serve para auxiliar o método get_products_ids a ter um formato de resposta   
class Product(BaseModel):
    product_id: str
    product_name: str

#esse trecho é para definir o ciclo de vida da API, de forma que o modelo do sistema de recomendação só é carregado uma vez na inicialização da API
@asynccontextmanager
async def lifespan(app: FastAPI):
    global sistema_carregado
    # Carrega o modelo na inicialização
    sistema_carregado = custom_load('/app/sistema_recomendacao_endpoint/sist_recomendacao.pkl')
    yield
    # Aqui poderia ser colocado o código de cleanup, se necessário

# Instancia a aplicação com lifespan configurado para dar carga no modelo uma vez só
app = FastAPI(lifespan=lifespan)

#metodo para a pagina inicial da API
@app.get("/", response_model=str)
async def root():
    """
    Exibe uma mensagem de boas-vindas na página inicial.
    """
    return "Bem-vindo à API de Recomendação de Produtos! Essa API contém dois métodos. Eles estão listados no link: localhost:8000/docs"


#aqui definimos o método de recomendar
@app.get("/recomenda_produtos", response_model=List[Any])
async def recomenda_produtos(product_id: str):
    """
    Retorna os produtos recomendados.

    Precisa entrar com o identificador do produto, a lista de identificadores pode ser obtida no método /get_products_ids
    """
    return sistema_carregado.recomendar(product_id)

#aqui definimos o método para retornar todos os ids dos produtos
@app.get("/get_products_ids", response_model=List[Product])
async def get_products_ids():
    """
    Retorna a lista de IDs dos produtos.
    """
    return [{"product_id": p[0], "product_name": p[1]} for p in sistema_carregado.listar_produtos()]
