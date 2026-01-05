import requests

def fetch_external_data(token):
    url = "https://api.example.com/protected-resource"
    headers = {
        "Authorization": token
    }
    response = requests.get(
        url, 
        headers=headers,
        timeout=10,
    )
    response.raise_for_status()
    return response.json()