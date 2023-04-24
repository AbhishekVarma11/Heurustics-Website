import os
from sqlalchemy import create_engine, text

# Create the database connection URL
my_secret = os.environ['DB_CONNECTION_STRING']

# Create the database engine
engine = create_engine(my_secret,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    column_names = result.keys()

  jobs = []

  for row in result.all():
    jobs.append(dict(zip(column_names, row)))

  return jobs


def load_job_from_job(id):
  with engine.connect() as conn:
    result = conn.execute(text(f"select * from jobs where id={id}"))
    #column_names = result.keys()
    rows=[]
    for row in result.all():
      rows.append(row._mapping)
    if len(rows) == 0:
      return None
    else:
      return [dict(row) for row in rows]
