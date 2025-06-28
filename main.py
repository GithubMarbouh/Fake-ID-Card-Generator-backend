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