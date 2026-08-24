import json
import os
from datetime import datetime, timezone
from pathlib import Path
import requests

# The URL specified in the README
API_URL = "https://jsonplaceholder.typicode.com/posts"

print(f"Fetching data from {API_URL}...")

# 1 & 2. Send GET request with a timeout of 20 seconds
response = requests.get(API_URL, timeout=20)

# 3. Check status code and fail clearly if unsuccessful
response.raise_for_status()

print("Status Code:", response.status_code)

# 4. Print Content-Type header
print("Content-Type:", response.headers.get("Content-Type"))

# 5. Parse the JSON response
payload = response.json()

# 6. Determine top-level JSON structure
print("Top-level type:", type(payload).__name__)

# 7 & 8. Print number of records and a sample record
if isinstance(payload, list):
    print("Number of records:", len(payload))
    if len(payload) > 0:
        print("\n--- Sample Record ---")
        print(json.dumps(payload[0], indent=2))
elif isinstance(payload, dict):
    print("Number of keys/records:", len(payload))
    if len(payload) > 0:
        print("\n--- Sample Record ---")
        sample_key = list(payload.keys())[0]
        print(json.dumps({sample_key: payload[sample_key]}, indent=2))

# 9. Save the raw response to data/raw/api_snapshot.json
output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True) # Creates the 'raw' folder if it doesn't exist
output_path = output_dir / "api_snapshot.json"

with open(output_path, "w", encoding="utf-8") as f:
    json.dump(payload, f, indent=2, ensure_ascii=False)

print(f"\nSaved snapshot to: {output_path}")

# 10. Record the retrieval timestamp in UTC
utc_now = datetime.now(timezone.utc).isoformat()
print("\nRetrieval timestamp (UTC):", utc_now)
print("-> IMPORTANT: Copy this timestamp into docs/source_inventory.md!")