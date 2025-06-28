# Utiliser Python 3.10
FROM python:3.10.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers requirements
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code source
COPY . .

# Créer le dossier pour les images générées
RUN mkdir -p generated_images

# Exposer le port
EXPOSE 8000

# Variable d'environnement pour Replicate
ENV REPLICATE_API_TOKEN=""

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]