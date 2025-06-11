import requests
from bs4 import BeautifulSoup
import pandas as pd
import os

def scrape_jobs():
    url = "https://example.com/jobs"  # Ganti dengan situs target
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    jobs = []

    for job_element in soup.select(".job-posting"):  # Ganti selector sesuai target
        title = job_element.select_one(".job-title").text.strip() if job_element.select_one(".job-title") else "N/A"
        company = job_element.select_one(".company-name").text.strip() if job_element.select_one(".company-name") else "N/A"
        location = job_element.select_one(".location").text.strip() if job_element.select_one(".location") else "N/A"
        salary = job_element.select_one(".salary").text.strip() if job_element.select_one(".salary") else "N/A"

        jobs.append({
            "title": title,
            "company": company,
            "location": location,
            "salary_raw": salary
        })

    df = pd.DataFrame(jobs)
    os.makedirs("../../data", exist_ok=True)
    df.to_csv("../../data/live_jobs.csv", index=False)
