from dotenv import load_dotenv
import os

load_dotenv()
print(os.getenv("my_key"))
print(os.getenv("model"))