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

    def download_file(self, file_id, save_path=None):
        """
        Download a file by ID from the API.
        If save_path is provided, saves to disk.
        Otherwise returns bytes content.
        """
        response = requests.get(
            f"{self.api_url}/download/{file_id}",
            headers=self.headers,
            stream=True
        )
        response.raise_for_status()

        if save_path:
            with open(save_path, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return save_path
        else:
            return response.content
