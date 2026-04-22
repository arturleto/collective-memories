#!/usr/bin/env python3
import subprocess, requests, base64, json, os

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(OUTPUT_DIR, exist_ok=True)

PROJECT = "gen-lang-client-0513605051"
LOCATION = "us-central1"
MODEL = "imagen-4.0-generate-001"
ENDPOINT = f"https://{LOCATION}-aiplatform.googleapis.com/v1/projects/{PROJECT}/locations/{LOCATION}/publishers/google/models/{MODEL}:predict"

def get_token():
    return subprocess.check_output(["gcloud", "auth", "application-default", "print-access-token"]).decode().strip()

def gen(name, prompt):
    token = get_token()
    payload = {
        "instances": [{"prompt": prompt}],
        "parameters": {"sampleCount": 1, "aspectRatio": "16:9", "outputMimeType": "image/png"}
    }
    r = requests.post(ENDPOINT, json=payload, headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"})
    r.raise_for_status()
    data = r.json()["predictions"][0]["bytesBase64Encoded"]
    path = os.path.join(OUTPUT_DIR, f"{name}.png")
    with open(path, "wb") as f:
        f.write(base64.b64decode(data))
    print(f"✅ Saved: {path}")
    return path

prompts = [
    ("hero_phone", "Sleek modern smartphone floating in deep dark midnight blue cosmic space, glowing golden light particles and small glowing coins orbiting around it, photographic shutter burst effect, luxury premium aesthetic, cinematic dramatic lighting, ultra high-end feel, dark navy background with subtle galaxy dust, no text, no people"),
    ("how_it_works", "Close up of hands holding smartphone camera photographing a tropical Bali rice terrace at golden sunset hour, tiny glowing gold coins and light particles materializing and floating out from the phone screen, luxury travel aesthetic, deep midnight navy and warm gold color palette, cinematic bokeh, no text"),
    ("earnings", "Futuristic holographic financial dashboard floating in dark midnight blue space, glowing green upward chart with golden highlights, stacked shiny USDC coin tokens with soft purple blue neon glow, abstract luxury geometric prisms in background, wealth and success visual, ultra premium dark navy aesthetic, cinematic volumetric light, no text"),
    ("community", "Diverse group of happy young people in Bali tropical setting each holding smartphones up photographing the world around them, golden light glowing from phone screens, premium lifestyle aesthetic, warm tropical sunset, deep navy blue sky background, cinematic shot, no text, photorealistic"),
]

for name, prompt in prompts:
    print(f"Generating {name}...")
    try:
        gen(name, prompt)
    except Exception as e:
        print(f"❌ {name}: {e}")
