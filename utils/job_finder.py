# import os
# from dotenv import load_dotenv
# import requests

# load_dotenv()
# RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")



# def find_jobs(query, location, job_type=None, page=1):
#     url = "https://jsearch.p.rapidapi.com/search"
#     headers = {
#         "X-RapidAPI-Key": "RAPIDAPI_KEY",
#         "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
#     }

#     params = {
#         "query": query,
#         "page": page,
#         "num_pages": 1,
#         "remote_jobs_only": "true" if location.lower() == "remote" else "false"
#     }

#     if job_type and job_type != "Any":
#         params["job_type"] = job_type

#     if location.lower() != "remote":
#         params["location"] = location

#     response = requests.get(url, headers=headers, params=params)
#     response.raise_for_status()
#     data = response.json()

#     return data.get("data", [])
# import requests
# import os
# from dotenv import load_dotenv

# load_dotenv()

# def find_jobs(query, location="Remote", job_type=None, page=1, num_pages=1):
#     """
#     Calls the JSearch API on RapidAPI to find jobs.
#     """

#     RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
#     RAPIDAPI_HOST = os.getenv("RAPIDAPI_HOST", "jsearch.p.rapidapi.com")

#     if not RAPIDAPI_KEY:
#         raise Exception("❌ RAPIDAPI_KEY not found. Please set it in your .env file.")

#     # Compose query string
#     if location.lower() != "remote":
#         q = f"{query} {location}"
#     else:
#         q = query

#     params = {
#         "query": q,
#         "page": page,
#         "num_pages": num_pages,
#         "remote_jobs_only": "true" if location.lower() == "remote" else "false"
#     }

#     url = "https://jsearch.p.rapidapi.com/search"
#     headers = {
#         "X-RapidAPI-Key": RAPIDAPI_KEY,
#         "X-RapidAPI-Host": RAPIDAPI_HOST
#     }

#     response = requests.get(url, headers=headers, params=params, timeout=10)

#     if response.status_code == 200:
#         data = response.json()
#         return data.get("data", [])
#     else:
#         raise Exception(f"API Error: {response.status_code} {response.reason} - {response.text}")




import os
import requests
import sqlite3
from dotenv import load_dotenv

load_dotenv()

def init_db():
    """
    Initializes the jobs.db and creates the jobs table if not exists.
    """
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jobs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            job_id TEXT,
            title TEXT,
            company TEXT,
            location TEXT,
            description TEXT,
            apply_link TEXT,
            logo_url TEXT
        )
    """)
    conn.commit()
    conn.close()


def save_jobs_to_db(jobs):
    """
    Save a list of jobs to the SQLite database.
    """
    conn = sqlite3.connect("jobs.db")
    cursor = conn.cursor()
    for job in jobs:
        cursor.execute("""
            INSERT INTO jobs (job_id, title, company, location, description, apply_link, logo_url)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            job.get("job_id"),
            job.get("job_title"),
            job.get("employer_name"),
            f"{job.get('job_city', '')}, {job.get('job_country', '')}",
            job.get("job_description", "")[:500],
            job.get("job_apply_link"),
            job.get("employer_logo")
        ))
    conn.commit()
    conn.close()


def find_jobs(query, location="Remote", job_type=None, page=1, num_pages=1):
    """
    Calls the JSearch API on RapidAPI to find jobs.
    """
    init_db()

    RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")
    if not RAPIDAPI_KEY:
        raise Exception("RAPIDAPI_KEY not found in .env file")

    RAPIDAPI_HOST = "jsearch.p.rapidapi.com"

    q = f"{query} in {location}"
    params = {
        "query": q,
        "page": page,
        "num_pages": num_pages,
        "remote_jobs_only": "true" if location.lower() == "remote" else "false"
    }

    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": RAPIDAPI_HOST
    }

    response = requests.get(url, headers=headers, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()
        jobs = data.get("data", [])
        save_jobs_to_db(jobs)
        return jobs
    else:
        raise Exception(f"API Error: {response.status_code} {response.reason}")

