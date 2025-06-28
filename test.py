# import requests

# url = "http://localhost:8002/generate-image/"
# data = {
#     # Realistic photo of an ID photo of a brown-haired woman around 40 years old.
#     # Realistic photo of a passport-style photo of a woman with short blonde hair in her early 40s
#     # High-quality ID photo of a man with dark skin and a bald head, around 35 years old.

#     #prompts:
#     # Realistic photo of a passport-style photo of a woman with short blonde hair in her early 40s.
#     # High-quality ID photo of a man with dark skin and a bald head, around 35 years old.
#     # Professional photo of a middle-aged woman with curly red hair, wearing glasses, taken for identification purposes.
#     # Realistic ID-style photo of a man with a trimmed beard and straight black hair, around 45 years old.
#     #Portrait-style photo of a woman in her late 30s with shoulder-length brown hair, wearing a neutral expression,
#     "prompt": "Professional photo of a middle-aged woman with curly red hair, wearing glasses, taken for identification purposes. \"FLUX 1.1 Pro\"",
#     "prompt_upsampling": True
# }

# # Générer une image
# response = requests.post(url, json=data)

# # Récupérer le nom du fichier depuis les headers
# filename = response.headers['Content-Disposition'].split('filename=')[1]

# # Sauvegarder l'image reçue
# with open(filename, "wb") as f:
#     f.write(response.content)

# # Lister toutes les images générées
# response = requests.get("http://localhost:8000/list-images")
# print(response.json())

curl -X POST http://13.49.72.13:8000/generate-image/ \
-H "Content-Type: application/json" \
-d '{"prompt": "Realistic photo of a passport-style photo of a woman with short blonde hair in her early 40s \"FLUX 1.1 Pro\"", "prompt_upsampling": true}' \
--output image_generee.png

# --version1
# import requests

# url = "http://localhost:8000/generate-image/"
# data = {
#     "prompt": "photo realiste d'une photo d'identite  d'un homme  de 20 ans, fond noir, haute  \"FLUX 1.1 Pro\"",
#     "prompt_upsampling": True
# }

# response = requests.post(url, json=data)

# # Sauvegarder l'image reçue en PNG
# with open("image_generee.png", "wb") as f:
#     f.write(response.content)


import requests
import os
from datetime import datetime

# URL de l'API
API_URL = "http://localhost:8001/generate-image/"

# Données pour la requête
data = {
    "prompt": "Realistic ID-style photo of a man with a trimmed beard and straight black hair, around 80 years old",
    "prompt_upsampling": True
}

# Répertoire pour sauvegarder les images
SAVE_DIR = "generated_images"
if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

try:
    # Faire la requête POST
    response = requests.post(API_URL, json=data)
    
    # Vérifier si la requête a réussi
    response.raise_for_status()
    
    # Générer un nom de fichier unique avec un timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"generated_image_{timestamp}.png"
    filepath = os.path.join(SAVE_DIR, filename)
    
    # Sauvegarder l'image
    with open(filepath, 'wb') as f:
        f.write(response.content)
    
    print(f"Image sauvegardée avec succès: {filepath}")

except requests.exceptions.RequestException as e:
    print(f"Erreur lors de la requête: {e}")
    if hasattr(e, 'response') and e.response is not None:
        print(f"Détails de l'erreur: {e.response.text}")
except Exception as e:
    print(f"Erreur inattendue: {e}")