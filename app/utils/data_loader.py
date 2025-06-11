import pandas as pd
import os

def load_job_data():
    path = os.path.join(os.path.dirname(__file__), "../../data/live_jobs.csv")
    if not os.path.exists(path):
        return pd.DataFrame(columns=["title", "company", "location", "salary_raw"])
    return pd.read_csv(path)
