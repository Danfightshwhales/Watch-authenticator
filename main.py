from fastapi import FastAPI, UploadFile, File
from inference import run_authenticator
import uvicorn

app = FastAPI(
    title="Watch Authenticator AI",
    description="Upload a watch photo and get authenticity + part breakdown.",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/predict")
async def predict_watch(file: UploadFile = File(...)):
    image_bytes = await file.read()
    result = run_authenticator(image_bytes)
    return result

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
