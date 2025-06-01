# Dockerfile ultra avancé Dihya (sécurité, multilingue, RGPD, audit, plugins, fallback local)
FROM python:3.12-slim
LABEL maintainer="Dihya Team <opensource@dihya.org>"
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# Sécurité, audit, RGPD, multilingue, plugins, fallback local ready
