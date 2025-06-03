import requests


class PreEpiSeizuresDBClient:
    def __init__(self, api_url, username, password):
        self.api_url = api_url.rstrip("/")
        self.token = self._get_token(username, password)
        self.headers = {"Authorization": f"Bearer {self.token}"}

    def _get_token(self, username, password):
        response = requests.post(
            f"{self.api_url}/token",
            data={"username": username, "password": password}
        )
        response.raise_for_status()
        return response.json()["access_token"]

    def get_files(self, min_events=0):
        response = requests.get(
            f"{self.api_url}/files",
            headers=self.headers,
            params={"min_events": min_events}
        )
        response.raise_for_status()
        return response.json()
