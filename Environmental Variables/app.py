import os
from dotenv import load_dotenv

load_dotenv()


database = os.getenv('DATABASE')
print(database)
