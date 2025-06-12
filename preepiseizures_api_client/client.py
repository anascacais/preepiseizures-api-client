import requests
import os


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

    def download_record(self, record_id, save_path=None):
        """
        Download a record by ID from the API.
        If save_path is provided, saves to disk.
        Otherwise returns bytes content.
        """
        response = requests.get(
            f"{self.api_url}/download/{record_id}",
            headers=self.headers,
            stream=True
        )
        response.raise_for_status()

        content_disposition = response.headers['content-disposition']
        filename = content_disposition.split("filename=")[-1].strip('";')

        if save_path:
            with open(os.path.join(save_path, filename), "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            print(f"File saved as: {os.path.join(save_path, filename)}")
            return os.path.join(save_path, filename)
        else:
            return response.content

    def download_records(self, record_ids, save_zip_path):
        # Pass file_ids as multiple query parameters ?file_ids=1&file_ids=2
        params = [("record_ids", fid) for fid in record_ids]
        response = requests.get(
            f"{self.api_url}/download",
            headers=self.headers,
            params=params,
            stream=True
        )
        response.raise_for_status()
        content_disposition = response.headers['content-disposition']
        zipname = content_disposition.split("filename=")[-1].strip('";')

        with open(os.path.join(save_zip_path, zipname), "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"ZIPs saved as: {os.path.join(save_zip_path, zipname)}")

    def get_sessions_by_patient(self, patient_code):
        response = requests.get(
            f"{self.api_url}/patients/{patient_code}/sessions",
            headers=self.headers,
        )
        response.raise_for_status()
        return response.json()

    def get_records(self, patient_code=None, session_date=None, modality=None):
        response = requests.get(
            f"{self.api_url}/records",
            headers=self.headers,
            params={"patient_code": patient_code,
                    "session_date": session_date, "modality": modality}
        )
        response.raise_for_status()
        return response.json()

    def get_events(self, patient_code=None, session_date=None, session_id=None):
        response = requests.get(
            f"{self.api_url}/events",
            headers=self.headers,
            params={"patient_code": patient_code,
                    "session_date": session_date, "session_id": session_id}
        )
        response.raise_for_status()
        return response.json()
