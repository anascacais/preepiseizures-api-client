from preepiseizures_api_client.client import PreEpiSeizuresDBClient

client = PreEpiSeizuresDBClient(
    "http://localhost:8000", "testuser", "mypassword")

# Get records
records = [item['record_id'] for item in client.get_records(
    patient_code='IQCX', modality='report')]
print(records)

# Download file and save locally
_ = client.download_record(
    records[0], save_path="results")

# Download multiple files as ZIP
client.download_records(records, "results")

# Get sessions by patient
sessions = client.get_sessions_by_patient(patient_code='IQCX')
print(sessions)

# Get events
events = client.get_events(
    patient_code='IQCX', session_date='2021-06-14 09:00:00')
print(events)
