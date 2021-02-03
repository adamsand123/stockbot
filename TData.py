import os
from dotenv import load_dotenv
import requests
import json


class TData:
    """
    https://twelvedata.com/docs
    """

    def __init__(self):
        load_dotenv()
        self.token = os.getenv('12DATA_TOKEN')
        # options: 1min, 5min, 15min, 30min, 45min, 1h, 2h, 4h, 8h, 1day, 1week, 1month
        self.options = ['1min', '5min', '15min', '30min', '45min', '1h', '2h', '4h', '8h', '1day', '1week', '1month']

    def get_help(self, stock):
        return f"Usage: {stock} [" + " | ".join([option for option in self.options]) + "]"

    def get_meta(self, stock, interval=None):
        stock_json = None
        if interval is None:
            url = f'https://api.twelvedata.com/time_series?symbol={stock}&interval=1min&apikey={self.token}'
            stock_json = requests.get(url).json()
        elif interval in self.options:
            url = f'https://api.twelvedata.com/time_series?symbol={stock}&interval={interval}&apikey={self.token}'
            stock_json = requests.get(url).json()
        else:
            return self.get_help(stock)

        if stock_json is not None:
            tmp_str = json.dumps(stock_json["meta"], indent=4)
            return tmp_str

    def get_last3(self, stock, interval=None):
        stock_json = None
        if interval is None:
            url = f'https://api.twelvedata.com/time_series?symbol={stock}&interval=1min&apikey={self.token}'
            stock_json = requests.get(url).json()
        elif interval in self.options:
            url = f'https://api.twelvedata.com/time_series?symbol={stock}&interval={interval}&apikey={self.token}'
            stock_json = requests.get(url).json()
        else:
            return self.get_help(stock)

        if stock_json is not None:
            tmp_str = json.dumps(stock_json["values"][0], indent=4)
            newest_value = float(stock_json["values"][0]["open"])
            to_the_moon = True
            values = list()
            for n in range(1, 3):
                tmp_str += json.dumps(stock_json["values"][n], indent=4)
                values.append(float(stock_json["values"][n]["open"]))
            for value in values:
                if value > newest_value:
                    to_the_moon = False
            if to_the_moon:
                return tmp_str + "\nTOOOO THE MOOOOOOOOON!! DIAMOND HAAANDZZ"
            else:
                return tmp_str

if __name__ == '__main__':
    td = TData()
    print(td.get_last3('GME', '11min'))
