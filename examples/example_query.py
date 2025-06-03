from preepiseizures_api_client.client import PreEpiSeizuresDBClient

client = PreEpiSeizuresDBClient(
    "http://yourserver:8000", "myusername", "mypassword")
files = client.get_files(min_events=0)
print(files)
