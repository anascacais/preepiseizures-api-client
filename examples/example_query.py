from preepiseizures_api_client.client import PreEpiSeizuresDBClient

client = PreEpiSeizuresDBClient(
    "http://localhost:8000", "testuser", "mypassword")
files = client.get_files(min_events=0)
print(files)


# Download first file and save locally
file_id = files[0]['id']
local_path = client.download_file(file_id, save_path="downloaded_file.txt")
print(f"File saved to: {local_path}")


# Download multiple files as ZIP
file_ids = [f["id"] for f in files]
client.download_files(file_ids, "files.zip")