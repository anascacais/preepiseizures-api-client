from preepiseizures_api_client.client import PreEpiSeizuresDBClient
from config import HOST, USER, PASSWORD

client = PreEpiSeizuresDBClient(
    f"http://{HOST}:8000", USER, PASSWORD)

# # Get records
# records = [item['record_id'] for item in client.get_records(modality='report')]
# # Download multiple files as ZIP
# client.download_records(records, "results")


events = client.get_events(event_types=["aware", "focal"])
print(events)
