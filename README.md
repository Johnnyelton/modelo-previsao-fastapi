# modelo-previsao-fastapi

API de **modelo de previsão** pronta para subir no GitHub, rodar localmente, e fazer deploy.
Inclui `endpoints.json` com a descrição dos pontos de extremidade.

## Visão geral
- Framework: **FastAPI**
- Endpoints:
  - `GET /health` — verificação de saúde
  - `POST /predict` — retorna uma previsão e um score com base em 2–3 features numéricas
- Sem dependências de ML pesadas: uma lógica simples de scoring (ideal para teste técnico).

## Estrutura do projeto
```
modelo-previsao-fastapi/
├─ README.md
├─ endpoints.json
├─ requirements.txt
├─ Dockerfile
├─ .gitignore
└─ app/
   └─ main.py
```

## Rodando localmente
1. **Crie e ative** um ambiente virtual (opcional, mas recomendado):
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate
   # Linux/Mac:
   source .venv/bin/activate
   ```

2. **Instale dependências**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Suba o servidor**:
   ```bash
   uvicorn app.main:app --reload
   ```
   A API ficará em `http://127.0.0.1:8000` (docs interativas em `/docs`).

## Testes rápidos (curl)
```bash
# Health
curl -s http://127.0.0.1:8000/health

# Predict (2 features obrigatórias, a 3ª é opcional)
curl -s -X POST http://127.0.0.1:8000/predict \
  -H "Content-Type: application/json" \
  -d '{"feature_1": 1.2, "feature_2": 0.7, "feature_3": 0.5}'
```

Resposta esperada:
```json
{"prediction":"positive","score":1.41}
```

> **Regra do modelo**: `score = 0.7*feature_1 + 0.3*feature_2 + 0.1*feature_3 (se enviada)`  
> `prediction = "positive"` se `score >= 1.0`, senão `"negative"`.

## Docker (opcional)
```bash
docker build -t modelo-previsao-fastapi:latest .
docker run -p 8000:8000 modelo-previsao-fastapi:latest
```

## Deploy (exemplos)
- **Render**, **Railway**, **Fly.io**, **Azure Web Apps**, **Google Cloud Run** ou **AWS App Runner**.  
  Aponte o comando para `uvicorn app.main:app --host 0.0.0.0 --port $PORT` (a plataforma define `$PORT`).

## Criar o repositório no GitHub e enviar os arquivos
> *Você pode usar o nome abaixo ou escolher outro.*

1. No GitHub, clique **New repository** e crie o repositório (ex.: `modelo-previsao-fastapi`).
2. No seu computador:
   ```bash
   git init
   git add .
   git commit -m "feat: API de previsão (FastAPI) + endpoints.json"
   git branch -M main
   git remote add origin https://github.com/<SEU_USUARIO_GITHUB>/modelo-previsao-fastapi.git
   git push -u origin main
   ```

## `endpoints.json`
O arquivo **endpoints.json** descreve os pontos de extremidade (método, caminho, payloads e respostas).  
Edite conforme necessário — por exemplo, para adicionar novos campos no `/predict`.

## Como eu cheguei nessa etapa (passo a passo)
1. **Defini o escopo**: criar um protótipo de API de previsão simples e verificável.
2. **Escolhi FastAPI** por sua rapidez, tipagem via Pydantic e docs automáticas (Swagger em `/docs`).
3. **Modelei os endpoints**: `GET /health` e `POST /predict` com um payload mínimo.
4. **Implementei uma lógica de scoring** leve para simular um modelo de ML sem dependências pesadas.
5. **Documentei tudo** no `README.md` e gerei o `endpoints.json` com a especificação dos endpoints.
6. **Preparei o Dockerfile** e **requirements.txt** para facilitar execução local e deploy.
7. **Empacotei os arquivos** para você subir no GitHub e entregar o projeto.

---

**Licença**: MIT (adicione uma licença se desejar).
