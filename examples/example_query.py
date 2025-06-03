from preepiseizures_api_client.client import PreEpiSeizuresDBClient

client = PreEpiSeizuresDBClient(
    "http://localhost:8000", "testuser", "mypassword")
files = client.get_files(min_events=1)
print(files)
