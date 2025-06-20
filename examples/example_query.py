from preepiseizures_api_client.client import PreEpiSeizuresDBClient
from config import HOST, USER, PASSWORD

client = PreEpiSeizuresDBClient(
    f"http://{HOST}:8000", USER, PASSWORD)


# Get sessions by patient
sessions = client.get_sessions(
    patient_code='BBYZ', event_types=["aware", "focal"], modality='report')
print(sessions)

# Get records
records = [item['record_id'] for item in client.get_records(
    patient_code='IQCX', modality='report')]
print(records)

# Download file and save locally
_ = client.download_record(
    records[0], save_path="results")

# Download multiple files as ZIP
client.download_records(records, "results")


# Get events
events = client.get_events(
    patient_code='BBYZ', session_date='2020-09-22 10:00:00', event_types=["aware", "focal"])
print(events)
