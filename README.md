# Currículo Web com Docker

## O que foi feito

Criei uma aplicação web em Python com Flask que mostra meu currículo em uma página HTML bonita e responsiva.

A aplicação foi containerizada com Docker para rodar em qualquer computador.

## Tecnologias

- Python 3.11
- Flask (framework web)
- HTML/CSS
- Docker

## Arquivos do Projeto

```
projeto-curriculo/
├── app.py              # Aplicação Flask
├── Dockerfile          # Configuração do container
├── requirements.txt    # Dependências Python
├── README.md          # Este arquivo
└── templates/
    └── index.html     # Página do currículo
```

## Como executar (Windows)

### 1. Baixar e executar a imagem do Docker Hub

```bash
docker pull SEU_USERNAME/curriculo-web:latest
docker run -d -p 8080:80 --name meu-curriculo SEU_USERNAME/curriculo-web:latest
```

Abra o navegador em: http://localhost:8080

### 2. Ou construir localmente

```bash
# Entrar na pasta do projeto
cd projeto-curriculo

# Construir a imagem
docker build -t curriculo-web .

# Executar o container
docker run -d -p 8080:80 --name nome-curriculo-legal curriculo-web
```

Abra o navegador em: http://localhost:8080

## Imagem no Docker Hub

Link da imagem: https://hub.docker.com/r/SEU_USERNAME/curriculo-web

Para usar:
```bash
docker pull SEU_USERNAME/curriculo-web:latest
```

## Comandos úteis

```bash
# Ver containers rodando
docker ps

# Parar o container
docker stop meu-curriculo

# Remover o container
docker rm meu-curriculo

# Ver logs
docker logs meu-curriculo
```

## Dockerfile

O Dockerfile configura:
- Imagem base: Python 3.11
- Instala o Flask
- Copia os arquivos da aplicação
- Expõe a porta 80
- Inicia a aplicação automaticamente

## Requisitos atendidos

- Aplicação web em Python com Flask
- Página HTML com currículo
- Dockerfile completo
- Imagem publicada no Docker Hub
- Porta 80 exposta
- Aplicação funciona em container
