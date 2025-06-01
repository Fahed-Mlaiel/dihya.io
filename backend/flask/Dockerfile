# Dihya Coding Backend - Dockerfile ultra sécurisé
FROM python:3.11-slim
LABEL maintainer="Dihya Team <opensource@dihya.org>"
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY app ./app
COPY requirements.txt ./requirements.txt
COPY run.py ./run.py
# Correction : copie récursive du dossier app dans /app/app pour garantir la présence de tous les modules
COPY ./app /app/app
RUN pip install --upgrade pip && pip install -r requirements.txt
EXPOSE 5000
HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 CMD curl -f http://localhost:5000/api/health || exit 1
CMD ["python", "run.py"]
