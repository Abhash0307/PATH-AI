





import streamlit as st
from utils.job_finder import find_jobs
import json
import os
from datetime import datetime

st.set_page_config(page_title="💼 Job Finder", page_icon="💼", layout="wide")

st.title("💼 Job Finder")

st.markdown(
    """
    Search for remote or on-site jobs tailored to your skills.  
    Save jobs you're interested in, mark them as applied, or remove them.
    """
)

query = st.text_input("🔍 Job Title or Keywords", placeholder="E.g., Python Developer")

location_options = [
    "Remote", "United States", "Canada", "United Kingdom", "Germany", "India", "Australia", "Singapore", "France", 
    "Japan", "China", "Brazil", "Mexico", "South Africa", "Netherlands", "Sweden", "Norway", "Italy", "Spain"
]
location = st.selectbox("📍 Location", options=location_options, index=0)

job_types = ["Any", "Full-time", "Part-time", "Contract", "Internship", "Temporary", "Volunteer"]
job_type = st.selectbox("💼 Job Type", options=job_types, index=0)

SAVE_FILE = "saved_data/saved_jobs.json"
os.makedirs("saved_data", exist_ok=True)

def save_job(job):
    saved_jobs = []
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            saved_jobs = json.load(f)
    job["_saved_at"] = datetime.now().isoformat()
    job["_applied"] = False
    saved_jobs.append(job)
    with open(SAVE_FILE, "w") as f:
        json.dump(saved_jobs, f, indent=2)

def load_saved_jobs():
    if os.path.exists(SAVE_FILE):
        with open(SAVE_FILE, "r") as f:
            return json.load(f)
    return []

def remove_job(index):
    saved_jobs = load_saved_jobs()
    if 0 <= index < len(saved_jobs):
        removed_job = saved_jobs.pop(index)
        with open(SAVE_FILE, "w") as f:
            json.dump(saved_jobs, f, indent=2)
        return removed_job
    return None

def mark_applied(index):
    saved_jobs = load_saved_jobs()
    if 0 <= index < len(saved_jobs):
        saved_jobs[index]["_applied"] = True
        saved_jobs[index]["_applied_at"] = datetime.now().isoformat()
        with open(SAVE_FILE, "w") as f:
            json.dump(saved_jobs, f, indent=2)
        return saved_jobs[index]
    return None

tab1, tab2 = st.tabs(["🔍 Search Jobs", "💾 Saved Jobs"])

with tab1:
    if st.button("🔎 Search Jobs") and query.strip():
        with st.spinner("Searching..."):
            try:
                jobs = find_jobs(
                    query=query.strip(), 
                    location=location, 
                    job_type=None if job_type == "Any" else job_type
                )

                if not jobs:
                    st.info("🚫 No jobs found. Try another keyword or adjust filters.")
                else:
                    for i, job in enumerate(jobs):
                        col1, col2 = st.columns([4, 1])
                        with col1:
                            if job.get("employer_logo"):
                                st.image(job["employer_logo"], width=80)

                            st.subheader(job.get("job_title", "Job Title Not Available"))
                            st.write(f"**Company:** {job.get('employer_name', 'N/A')}")
                            st.write(f"**Location:** {job.get('job_city', '')}, {job.get('job_country', '')}")
                            st.write(f"**Job Type:** {job.get('job_type', 'N/A')}")

                            posted_at = job.get("job_posted_at")
                            if posted_at:
                                try:
                                    dt = datetime.fromisoformat(posted_at)
                                    st.write(f"📅 **Posted At:** {dt.strftime('%Y-%m-%d')}")
                                except Exception:
                                    st.write(f"📅 **Posted At:** {posted_at}")

                            desc = job.get("job_description", "")
                            st.write(f"**Description:** {desc[:300]}{'...' if len(desc) > 300 else ''}")

                            if job.get("job_apply_link"):
                                st.markdown(f"[🌐 Apply Here]({job['job_apply_link']})")

                        with col2:
                            if st.button(f"💾 Save Job {i+1}", key=f"save_{i}"):
                                save_job(job)
                                st.success(f"✅ Saved job: {job.get('job_title', 'N/A')}")
            except Exception as e:
                st.error(f"❌ {e}")
    else:
        st.info("Enter a keyword and click **Search Jobs** to begin.")

with tab2:
    st.header("💾 Saved Jobs")

    saved_jobs = load_saved_jobs()

    if not saved_jobs:
        st.info("You haven’t saved any jobs yet.")
    else:
        saved_jobs = sorted(saved_jobs, key=lambda x: x.get("_saved_at", ""), reverse=True)

        for idx, job in enumerate(saved_jobs):
            col1, col2 = st.columns([4, 1])
            with col1:
                if job.get("employer_logo"):
                    st.image(job["employer_logo"], width=80)

                st.subheader(job.get("job_title", "Job Title Not Available"))
                st.write(f"**Company:** {job.get('employer_name', 'N/A')}")
                st.write(f"**Location:** {job.get('job_city', '')}, {job.get('job_country', '')}")
                st.write(f"**Job Type:** {job.get('job_type', 'N/A')}")

                posted_at = job.get("job_posted_at")
                if posted_at:
                    try:
                        dt = datetime.fromisoformat(posted_at)
                        st.write(f"📅 **Posted At:** {dt.strftime('%Y-%m-%d')}")
                    except Exception:
                        st.write(f"📅 **Posted At:** {posted_at}")

                saved_at = job.get("_saved_at")
                if saved_at:
                    dt_saved = datetime.fromisoformat(saved_at)
                    st.write(f"💾 **Saved At:** {dt_saved.strftime('%Y-%m-%d %H:%M')}")

                applied_status = "✅ Applied" if job.get("_applied") else "❌ Not Applied"
                st.write(f"📌 **Status:** {applied_status}")

                if job.get("_applied") and job.get("_applied_at"):
                    dt_applied = datetime.fromisoformat(job["_applied_at"])
                    st.write(f"🗓️ **Applied At:** {dt_applied.strftime('%Y-%m-%d %H:%M')}")

                desc = job.get("job_description", "")
                st.write(f"**Description:** {desc[:300]}{'...' if len(desc) > 300 else ''}")

                if job.get("job_apply_link"):
                    st.markdown(f"[🌐 Apply Here]({job['job_apply_link']})")

            with col2:
                if not job.get("_applied"):
                    if st.button(f"✅ Mark Applied", key=f"applied_{idx}"):
                        marked = mark_applied(idx)
                        if marked:
                            st.success(f"🎯 Marked as Applied: {marked.get('job_title', 'N/A')}")
                            st.experimental_rerun()
                if st.button(f"🗑️ Remove", key=f"remove_{idx}"):
                    removed = remove_job(idx)
                    if removed:
                        st.success(f"🗑️ Removed: {removed.get('job_title', 'N/A')}")
                        st.experimental_rerun()


