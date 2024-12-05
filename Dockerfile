#puxamos a imagem base que queremos usar
FROM python:3.12-slim

#definimos o diretorio
WORKDIR /app

#aqui trazemos o requirements.txt para o nosso diretorio
COPY ./requirements.txt /app/requirements.txt

#aqui instalamos as dependencias contidas no requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt


