
# --version2
# from fastapi import FastAPI, HTTPException
# from fastapi.responses import Response
# import replicate
# import io
# from PIL import Image
# from pydantic import BaseModel
# from datetime import datetime
# import os

# app = FastAPI()

# # Créer un dossier pour stocker les images si il n'existe pas
# UPLOAD_FOLDER = "generated_images"
# if not os.path.exists(UPLOAD_FOLDER):
#     os.makedirs(UPLOAD_FOLDER)

# class ImagePrompt(BaseModel):
#     prompt: str
#     prompt_upsampling: bool = True

# @app.post("/generate-image/")
# async def generate_image(image_prompt: ImagePrompt):
#     try:
#         input_data = {
#             "prompt": image_prompt.prompt,
#             "prompt_upsampling": image_prompt.prompt_upsampling
#         }
        
#         # Générer un nom de fichier unique basé sur le timestamp
#         timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
#         filename = f"image_{timestamp}.png"
#         filepath = os.path.join(UPLOAD_FOLDER, filename)
        
#         # Run the model
#         output = replicate.run(
#             "black-forest-labs/flux-1.1-pro",
#             input=input_data
#         )
        
#         # Read the image data
#         image_data = output.read()
        
#         # Convert WebP to PNG using PIL and save to file
#         with io.BytesIO(image_data) as webp_buffer:
#             with Image.open(webp_buffer) as img:
#                 # Sauvegarder l'image sur le disque
#                 img.save(filepath, format="PNG")
                
#                 # Créer aussi un buffer pour la réponse HTTP
#                 png_buffer = io.BytesIO()
#                 img.save(png_buffer, format="PNG")
#                 png_data = png_buffer.getvalue()
        
#         # Return the PNG image directly in the response
#         return Response(
#             content=png_data,
#             media_type="image/png",
#             headers={
#                 "Content-Disposition": f"attachment; filename={filename}",
#                 "X-Image-Path": filepath  # Ajouter le chemin de l'image dans les headers
#             }
#         )
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/health")
# async def health_check():
#     return {"status": "healthy"}

# # Endpoint pour lister toutes les images générées
# @app.get("/list-images")
# async def list_images():
#     try:
#         images = os.listdir(UPLOAD_FOLDER)
#         return {
#             "images": images,
#             "total": len(images),
#             "folder": UPLOAD_FOLDER
#         }
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/debug-token")
# async def debug_token():
#     return {"token": os.getenv("REPLICATE_API_TOKEN", "Non défini")}
# --version2
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response
import replicate
import io
from PIL import Image
from pydantic import BaseModel

app = FastAPI()

class ImagePrompt(BaseModel):
    prompt: str
    prompt_upsampling: bool = True

@app.post("/generate-image/")
async def generate_image(image_prompt: ImagePrompt):
    try:
        input_data = {
            "prompt": image_prompt.prompt,
            "prompt_upsampling": image_prompt.prompt_upsampling
        }
        
        # Run the model
        output = replicate.run(
            "black-forest-labs/flux-1.1-pro",
            input=input_data
        )
        
        # Read the image data
        image_data = output.read()
        
        # Convert WebP to PNG using PIL
        with io.BytesIO(image_data) as webp_buffer:
            # Open the WebP image
            with Image.open(webp_buffer) as img:
                # Create a new bytes buffer for PNG
                png_buffer = io.BytesIO()
                # Save as PNG to the buffer
                img.save(png_buffer, format="PNG")
                png_data = png_buffer.getvalue()
        
        # Return the PNG image directly in the response
        return Response(
            content=png_data,
            media_type="image/png",
            headers={
                "Content-Disposition": "attachment; filename=generated_image.png"
            }
        )
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health_check():
    return {"status": "healthy"}