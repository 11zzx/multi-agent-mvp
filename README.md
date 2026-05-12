# Multi-Agent MVP

## Backend

```bash
cd backend

python -m venv venv

source venv/bin/activate
# Windows:
# venv\Scripts\activate

pip install -r requirements.txt

cp .env.example .env
# 编辑 .env 填入 OpenAI Key

uvicorn main:app --reload
```

Backend:
http://localhost:8000

## Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:
http://localhost:3000
