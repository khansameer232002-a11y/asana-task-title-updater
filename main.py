import os
import requests
import datetime

ASANA_PAT = os.environ["ASANA_PAT"]
PROJECT_ID = os.environ["PROJECT_ID"]

headers = {
    "Authorization": f"Bearer {ASANA_PAT}"
}

today = datetime.datetime.utcnow().date()

tasks_url = f"https://app.asana.com/api/1.0/projects/{PROJECT_ID}/tasks"
response = requests.get(tasks_url, headers=headers)
tasks = response.json().get("data", [])

for task in tasks:
    task_id = task["gid"]
    task_details = requests.get(f"https://app.asana.com/api/1.0/tasks/{task_id}", headers=headers)
    task_data = task_details.json().get("data", {})

    name = task_data.get("name", "")
    created_at = task_data.get("created_at", "")

    try:
        created_date = datetime.datetime.fromisoformat(created_at[:-1]).date()
    except:
        continue

    if created_date != today:
        continue

    if name[:4].count("|") == 1 and name[0:1].isdigit():
        continue

    now = datetime.datetime.utcnow()
    date_code = f"{now.day}{now.strftime('%B')[0].upper()}"
    new_name = f"{date_code} | {name}"

    update_data = {"name": new_name}
    update = requests.put(f"https://app.asana.com/api/1.0/tasks/{task_id}", headers=headers, json=update_data)

    if update.status_code == 200:
        print(f"✅ Renamed task: {new_name}")
    else:
        print(f"❌ Failed to update {name}: {update.text}")