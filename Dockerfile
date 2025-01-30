# Utiliser une image officielle de Python
FROM python:3.12-slim

# Définir le répertoire de travail à /app
WORKDIR /app

# Copier les fichiers requirements.txt et app.py dans le répertoire de travail
COPY . /app

# Installer Flask
RUN pip install flask

# Exposer le port sur lequel Flask va tourner
EXPOSE 5005

# Définir la commande par défaut pour lancer l'application Flask
CMD ["python", "app.py"]
