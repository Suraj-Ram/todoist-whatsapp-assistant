import os
import requests
import json
import datetime

todoist_api_token = os.getenv("TODOIST_API_TOKEN")
todoist_api_url = "https://api.todoist.com/rest/v1"

print(f"Using Todoist API token: {todoist_api_token}")


def list_tasks():
    output = requests.get(f"{todoist_api_url}/tasks", headers={
        "Authorization": f"Bearer {todoist_api_token}"
    })

    return json.loads(output.text)


def get_projects():
    output = requests.get(f"{todoist_api_url}/projects", headers={
        "Authorization": f"Bearer {todoist_api_token}"
    })
    raw_projects = json.loads(output.text)
    projects = {}
    for raw_project in raw_projects:
        projects[str(raw_project["id"])] = {
            "name": raw_project["name"],
            "url": raw_project["url"]
        }
    return projects


def get_due_date(task):
    try:
        return task["due"]["date"]
    except:
        return False


def get_tasks_today():
    tasks_all = list_tasks()
    tasks_today = []
    today = datetime.date.today().strftime("%Y-%m-%d")
    for task in tasks_all:
        if get_due_date(task) == today:
            tasks_today.append(task)

    return tasks_today


def print_tasks(tasks):
    projects = get_projects()

    printed_tasks = ""

    for task in tasks:
        project_id = str(task["project_id"])

        printed_tasks = printed_tasks + (f"""
            Project: {projects[project_id]["name"]}
            Content {task["content"]}
            Due: {get_due_date(task)}
            
        """)

    return printed_tasks


if __name__ == "__main__":
    print(print_tasks(get_tasks_today()))
