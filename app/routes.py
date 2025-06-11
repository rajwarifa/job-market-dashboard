from flask import Blueprint, render_template
from .utils.scraper import scrape_jobs
from .utils.data_loader import load_job_data

views = Blueprint("views", __name__)

@views.route("/")
def index():
    scrape_jobs()  # ← Otomatis scrape setiap akses halaman
    df = load_job_data()
    now = "Live update"
    return render_template("index.html", tables=[df.to_html(classes='data', header="true")], now=now)
