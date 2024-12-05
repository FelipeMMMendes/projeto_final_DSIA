## Projeto Final de Desenvolvimento de Sistemas de IA

#### Identificação do grupo:

Felipe Martins Machado Mendes - 22251506  
Gabriel Barreto Carvalho Telles - 22251719  
Lucas Araujo de Alencar - 22251690  
Pedro Gabriel Neves da Silva - 22251715  

### Como rodar o projeto:

Para rodar o projeto, é preciso ter o docker instalado na máquina.

1º - Clone o repositório

2º - Suba o contêiner usando

```
docker compose up -d
```

3º - Após o ambiente começar a rodar, a documentação da API vai estar no endereço:

[localhost:8000/docs](localhost:8000/docs)

Desenvolvemos dois métodos: 

- **/recomenda_produtos** - Insere o id de um produto e o sistema vai retornar outros semelhantes à ele.

- **/get_products_ids** - Retorna a lista com os ids dos produtos e os seus nomes. 

Estes métodos podem ser usados através da documentação ou através de seus endpoints. Recomendamos pegar os ids dos produtos primeiro para depois usá-los no outro método.

Endpoints dos métodos:

http://localhost:8000/get_products_ids

http://localhost:8000/recomenda_produtos?product_id=B096MSW6CT

Nesse exemplo acima do método de recomendação, o product id é B096MSW6CT, ele aceita apenas um product id por vez.




