from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import boto3

session = boto3.Session(profile_name='RecommenderTeam-416145492279', region_name='ap-southeast-1')

app = FastAPI()

# Configure CORS settings
origins = ["*"]  # Update this list to allow requests from specific origins if needed

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/translate")
def translate_text(text: str = Query(..., min_length=1)):
    # Initialize AWS Translate client
    client = session.client('translate')

    # Translate the text to English
    response = client.translate_text(
        Text=text,
        SourceLanguageCode='auto',
        TargetLanguageCode='en'
    )

    # Extract the translated text from the response
    translated_text = response['TranslatedText']

    return {"translated_text": translated_text}
