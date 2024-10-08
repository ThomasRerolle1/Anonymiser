from fastapi import FastAPI
from pydantic import BaseModel
import spacy

# Initialiser l'application FastAPI
app = FastAPI()

# Charger le modèle SpaCy
nlp = spacy.load("en_core_web_lg")

# Définir un schéma de données pour les requêtes
class TextData(BaseModel):
    text: str

# Définir une route POST pour anonymiser le texte
@app.post("/anonymize")
async def anonymize(data: TextData):
    doc = nlp(data.text)
    anonymized_text = data.text
    # Anonymiser toutes les entités nommées dans le texte
    print(doc.ents)
    for ent in doc.ents:
        print(ent.label_)
        if ent.label_ == "PERSON":
            anonymized_text = anonymized_text.replace(ent.text, "[PERSON]")
        elif ent.label_ == "GPE":
            anonymized_text = anonymized_text.replace(ent.text, "[LOCATION]")
        elif ent.label_ == "DATE":
            anonymized_text = anonymized_text.replace(ent.text, "[DATE]")
        else :
            anonymized_text = anonymized_text.replace(ent.text, "[ANON]")
    return {"anonymized_text": anonymized_text}

