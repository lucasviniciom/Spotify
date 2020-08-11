import requests
import base64
import json
from secrets import *

# Step 1 - Authorization
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

# Encode as Base64
message = f"{clientId}:{clientSecret}"
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = f"Basic {base64Message}"
data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']

# Get playlist endpoint
"""
playlistId = "myPlaylistId"
playlistUrl = f"https://api.spotify.com/v1/playlists/{playlistId}"
headers = {
    "Authorization": "Bearer " + token
}

res = requests.get(url=playlistUrl, headers=headers)

print(json.dumps(res.json(), indent=2))
"""
"""
# Get audio features

audioId = "4aCsgwFhbZ8CmYAotK7W2B?si=Gsv55yXxTWqEvW7x4XKqFA"
audiofeatUrl = f"https://api.spotify.com/v1/audio-features/{audioId}"
headers = {
    "Authorization": "Bearer " + token
}

res_audio = requests.get(url=audiofeatUrl, headers=headers)
print(json.dumps(res_audio.json(), indent=2))
"""
# Get new releases

ReleaseUrl = f"https://api.spotify.com/v1/browse/new-releases"
headers = {
    "Authorization": "Bearer " + token
}

res_audio = requests.get(url=ReleaseUrl, headers=headers)
print(json.dumps(res_audio.json(), indent=2))
