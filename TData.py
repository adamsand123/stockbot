import os
from dotenv import load_dotenv
import requests


class TData:
    """
    https://twelvedata.com/docs
    """
    def __init__(self):
        load_dotenv()
        self.token = os.getenv('12DATA_TOKEN')

    def get_value(self,symbol):
        url = f'https://api.twelvedata.com/time_series?symbol={symbol}&interval=1min&apikey={self.token}'
        resp = requests.get(url)
        return resp.json()['values'][0]


if __name__ == '__main__':
    td = TData()
    print(td.get_value('GME'))
