FROM python:3.11.2

# Définir les variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PORT=5000

# Créer un utilisateur non-root
RUN useradd -m appuser

# Définir le répertoire de travail
WORKDIR /app

# Copier les fichiers de dépendances
COPY requirements.txt .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copier le code de l'application
COPY . .

# Créer le dossier static s'il n'existe pas
RUN mkdir -p static

# Donner les permissions à appuser
RUN chown -R appuser:appuser /app
USER appuser

# Exposer le port
EXPOSE $PORT

# Commande pour démarrer l'application
CMD ["python", "app.py"]