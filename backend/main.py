from fastapi import FastAPI
from pydantic import BaseModel, HttpUrl
from fastapi.middleware.cors import CORSMiddleware
import toml

from services.genai import (
    YoutubeProcessor,
    GeminiProcessor
)

class VideoAnalysisRequest(BaseModel):
    youtube_link: HttpUrl
    # advanced settings

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze_video")
def analyze_video(request: VideoAnalysisRequest):
    with open("secrets.toml", "r") as s:
        secrets = toml.load(s)

    project = secrets["google_cloud"]["project_id"]

    genai_processor = GeminiProcessor(
        model_name = "gemini-pro",
        project = project
    )

    # Doing the analysis
    processor = YoutubeProcessor(genai_processor=genai_processor)
    result = processor.retrieve_youtube_documents(str(request.youtube_link), verbose=True)


    # summary = genai_processor.generate_document_summary(result, verbose=True)
    
    # It did not recognize group_size as a variable when it was a parameter
    group_size = 6

    # Find key concepts
    key_concepts = processor.find_key_concepts(result, group_size, verbose=True)
    
    return {
        "key_concepts": key_concepts
    }