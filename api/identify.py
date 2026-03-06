"""Vercel serverless function — Species Identifier (GPT-4o vision)"""
import os
import json
from http.server import BaseHTTPRequestHandler
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """You are a world-class field biologist and taxonomist working for BioJalisco, 
a biodiversity atlas project in Jalisco, Mexico. When shown a photo, identify the species with 
scientific precision but communicate in an engaging, accessible way.

You identify ALL living organisms — wild and domestic. For domestic animals like dogs, identify 
the specific breed (or mix). For cats, identify the breed. For garden plants, houseplants, 
livestock, pet birds, aquarium fish — identify them all with the same enthusiasm and detail. 
Every species has a story worth telling, whether it's a wild jaguar or a beloved family pet.

For dogs, always include breed-specific traits, temperament, and origin history in the description.
For mixed breeds, describe the likely mix and characteristics of each contributing breed.

Respond in this exact JSON format:
{
  "identification": {
    "common_name": "Common name or breed (English)",
    "nombre_comun": "Nombre común o raza (Spanish)",
    "scientific_name": "Genus species",
    "breed": "Specific breed if domestic animal, otherwise null"
  },
  "confidence": 85,
  "taxonomy": {
    "kingdom": "e.g. Animalia",
    "phylum": "e.g. Arthropoda",
    "class": "e.g. Insecta",
    "order": "e.g. Lepidoptera",
    "family": "e.g. Saturniidae",
    "genus": "e.g. Attacus",
    "species": "e.g. atlas"
  },
  "ecology": {
    "habitat": "Primary habitat description",
    "diet": "Feeding behavior",
    "size": "Typical size or dimensions",
    "lifespan": "Average lifespan",
    "behavior": "Key behavioral traits"
  },
  "geography": {
    "native_range": "Where the species originates",
    "found_in_jalisco": true/false,
    "found_in_mexico": true/false,
    "invasive": false
  },
  "conservation": {
    "iucn_status": "IUCN Red List status or 'Domesticated'",
    "population_trend": "Increasing|Stable|Decreasing|Unknown",
    "threats": "Primary threats, or 'None — domesticated species'"
  },
  "similar_species": [
    {
      "name": "Similar species common name",
      "scientific_name": "Genus species",
      "distinction": "How to tell them apart"
    }
  ],
  "description": "2-3 engaging sentences about the species. For domestic breeds include traits, temperament, origin.",
  "descripcion": "Same description in Spanish.",
  "fun_fact": "One surprising or delightful fact."
}

IMPORTANT RULES:
- "confidence" MUST be an integer from 0 to 100 representing your identification certainty percentage.
- "similar_species" should include 1-3 species that could be confused with this one.
- For domestic breeds, use "Domesticated" for iucn_status and describe breed-specific traits.
- All fields are required. Use "Unknown" for genuinely unknown values.

If the image doesn't contain a clearly identifiable organism, respond with:
{
  "error": "Brief explanation of why identification isn't possible.",
  "suggestion": "Tip for getting a better photo."
}

Always respond with valid JSON only, no markdown formatting."""


class handler(BaseHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)

        try:
            data = json.loads(body)
        except Exception:
            self._respond(400, {"error": "Invalid JSON"})
            return

        image_data = data.get('image_data', '')
        if not image_data:
            self._respond(400, {"error": "No image provided"})
            return

        # Strip data URI prefix if present
        if ',' in image_data:
            image_data = image_data.split(',', 1)[1]

        media_type = "image/jpeg"

        try:
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {
                        "role": "user",
                        "content": [
                            {"type": "text", "text": "Identify the species in this photo."},
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:{media_type};base64,{image_data}",
                                    "detail": "high"
                                }
                            }
                        ]
                    }
                ],
                max_tokens=1500,
                temperature=0.3
            )

            result_text = response.choices[0].message.content.strip()
            if result_text.startswith('```'):
                result_text = result_text.split('\n', 1)[1] if '\n' in result_text else result_text[3:]
                if result_text.endswith('```'):
                    result_text = result_text[:-3]
                result_text = result_text.strip()

            result = json.loads(result_text)
            self._respond(200, result)

        except Exception as e:
            self._respond(500, {"error": str(e)})

    def _respond(self, status, data):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
