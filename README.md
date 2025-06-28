# FastAPI Flux - Générateur d'images IA

## Description
API REST développée avec FastAPI pour la génération d'images à l'aide de l'IA. Ce projet utilise l'API Replicate pour générer des images à partir de prompts textuels avec le modèle Flux.

## Fonctionnalités
- 🎨 Génération d'images à partir de prompts textuels
- 📱 API REST simple et intuitive
- 💾 Sauvegarde automatique des images générées
- 🔧 Configuration Docker pour le déploiement
- ⚡ Interface rapide avec FastAPI

## Technologies utilisées
- **FastAPI 0.104.1** - Framework web moderne pour Python
- **Uvicorn** - Serveur ASGI haute performance
- **Replicate** - API pour l'IA générative
- **Pillow (PIL)** - Traitement d'images
- **Docker** - Containerisation

## Prérequis
- Python 3.8 ou supérieur
- Compte Replicate avec clé API
- Docker (optionnel, pour le déploiement)

## Installation
1. Clonez le projet :
   ```bash
   git clone <repo-url>
   cd fastapi-flux
   ```

2. Créez un environnement virtuel :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

4. Configurez votre clé API Replicate :
   ```bash
   export REPLICATE_API_TOKEN="your-api-token"
   ```

## Démarrage
### Démarrage local
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Démarrage avec Docker
```bash
docker build -t fastapi-flux .
docker run -p 8000:8000 -e REPLICATE_API_TOKEN="your-token" fastapi-flux
```

## Utilisation de l'API
### Endpoint principal
**POST** `/generate-image/`

**Corps de la requête :**
```json
{
  "prompt": "Description de l'image à générer",
  "prompt_upsampling": true
}
```

**Exemple avec curl :**
```bash
curl -X POST "http://localhost:8000/generate-image/" \
     -H "Content-Type: application/json" \
     -d '{
       "prompt": "A beautiful sunset over the mountains",
       "prompt_upsampling": true
     }'
```

## Structure du projet
```
fastapi-flux/
├── main.py                    # Application FastAPI principale
├── requirements.txt           # Dépendances Python
├── Dockerfile                # Configuration Docker
├── docker-compose.yml        # Configuration Docker Compose
├── test.py                   # Scripts de test
├── verif.py                  # Scripts de vérification
├── generated_images/         # Dossier des images générées
└── README.md
```

## Exemples d'images
Le dossier `generated_images/` contient des exemples d'images générées par l'API.

## Tests
Exécutez les tests avec :
```bash
python test.py
```

## Documentation interactive
Une fois l'application démarrée, accédez à :
- **Swagger UI** : http://localhost:8000/docs
- **ReDoc** : http://localhost:8000/redoc

## Variables d'environnement
- `REPLICATE_API_TOKEN` : Votre token d'authentification Replicate (obligatoire)

## Déploiement
Le projet inclut une configuration complète pour le déploiement avec Docker et Docker Compose.
# Fake-ID-Card-Generator-backend
