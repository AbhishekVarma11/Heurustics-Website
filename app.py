from flask import Flask, render_template, jsonify
from database import load_jobs_from_db, load_job_from_job
import json

app = Flask(__name__)


@app.route('/')
def hello_heurustics():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Heuristics')
@app.route("/api/jobs/<int:id>")
def show_job_api(id):
  jobs = load_job_from_job(id)
  return render_template('jobitem2.html',job=jobs)

@app.route("/jobs/<int:id>")
def show_job(id):
  job_details = load_job_from_job(id)
  #return jsonify(job)
  return render_template('jobpage.html',job_details=job_details)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
