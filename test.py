# import requests

# URL = "https://bcvtinztsqcolilikksy.supabase.co/functions/v1/fetch-transcripts"

# APIKEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJjdnRpbnp0c3Fjb2xpbGlra3N5Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjgzNDgwNzksImV4cCI6MjA4MzkyNDA3OX0.UuRTZs_Qf6q38AgvdbQezepNaw1dILq2JN-Q3Y0vf4c"

# headers = {
#     "accept": "*/*",
#     "content-type": "application/json",
#     "origin": "https://lennyshub.lovable.app",
#     "referer": "https://lennyshub.lovable.app/",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36",
#     "apikey": APIKEY,
#     "authorization": f"Bearer {APIKEY}",
#     "x-client-info": "supabase-js-web/2.90.1",
# }

# # IMPORTANT: body must be valid JSON.
# # Your DevTools shows content-length 12, which likely means something like {"page":1}
# # Try {"page":1} first (12 bytes). If it fails, switch to {}.
# payload = {"page": 1}

# r = requests.post(URL, headers=headers, json=payload, stream=True, timeout=120)
# print("Status:", r.status_code)
# if r.status_code >= 400:
#     print("Error:", r.text[:2000])
#     raise SystemExit(1)

# out = "fetch_transcripts_response.json"
# with open(out, "wb") as f:
#     for chunk in r.iter_content(chunk_size=1024 * 1024):
#         if chunk:
#             f.write(chunk)

# print("✅ Saved:", out)
# print("Content-Type:", r.headers.get("content-type"))
# print("Bytes:", r.headers.get("content-length"))
import json

with open("fetch_transcripts_response.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(type(data))
if isinstance(data, list):
    print("Items:", len(data))
elif isinstance(data, dict):
    print("Keys:", list(data.keys())[:20])
import json

with open("fetch_transcripts_response.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print("episodes in this response:", len(data.get("episodes", [])))
print("totalAvailable:", data.get("totalAvailable"))
print("slugs:", len(data.get("slugs", [])))
