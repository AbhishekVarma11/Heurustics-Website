from flask import Flask, render_template, jsonify
from database import load_jobs_from_db

app = Flask(__name__)
JOBS = [{
  'id': 1,
  'title': 'Backend Engineer',
  'location': 'new york',
  'Salary': '$120,000'
}, {
  'id': 2,
  'title': 'Cloud Engineer',
  'location': 'California',
  'Salary': '$150,000'
}, {
  'id': 3,
  'title': 'Devops Engineer',
  'location': 'Texas',
  'Salary': '$130,000'
}, {
  'id': 4,
  'title': 'Front-End Engineer',
  'location': 'Dalas',
}]


@app.route('/')
def hello_heurustics():
  jobs = load_jobs_from_db()
  return render_template('home.html', jobs=jobs, company_name='Heuristics')


@app.route("/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
