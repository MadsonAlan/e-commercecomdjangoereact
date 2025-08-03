#!/bin/sh

set -e

echo "Aguardando Postgres em $DB_HOST:$DB_PORT..."

until pg_isready -h "$DB_HOST" -p "$DB_PORT" -U "$DB_USER" > /dev/null 2>&1; do
  echo "Postgres ainda não está pronto — aguardando 2s..."
  sleep 2
done

echo "Postgres está pronto! Executando comando: $@"
exec "$@"
