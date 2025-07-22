#!/bin/sh

echo "Aplicando migrations..."
alembic revision --autogenerate -m "Initial migration"
alembic upgrade head

echo "Iniciando servidor..."
exec uvicorn app.main:app --host 0.0.0.0 --port 8000
