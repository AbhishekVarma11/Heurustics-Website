from sqlalchemy import create_engine, text

# Replace the values inside the quotes with your MySQL server details
db_username = "wds79edvl8dln0fxgto0"
db_password = "pscale_pw_1WbfNJjwT5VHzsOZeAyXOr0csLBr8XZDKiC5DEjScPS"
db_host = "aws.connect.psdb.cloud"
db_port = "3306"
db_name = "heurustics-careers-website"

# Create the database connection URL
db_url = f"mysql+pymysql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

# Create the database engine
engine = create_engine(db_url,
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
