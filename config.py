# Scheme: "postgres+psycopg2://<USERNAME>:<PASSWORD>@<IP_ADDRESS>:<PORT>/<DATABASE_NAME>"
from dotenv import load_dotenv
import os

from pathlib import Path  # python3 only
#
# env_path = Path('.') / '.env'
# load_dotenv(dotenv_path=env_path)
load_dotenv()

# DATABASE_URI = os.getenv('DATABASE_URI')


DATABASE_URI = 'postgres+psycopg2://postgres:fuk@my-postgres:5432/rpi_base'