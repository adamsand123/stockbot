import os
from dotenv import load_dotenv


class TData:
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('12DATA_TOKEN')
