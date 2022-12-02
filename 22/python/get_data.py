import requests
from datetime import datetime
import json


def get_session_cookie():
    with open("secret.json") as file:
        data = json.load(file)
    return data


def get_day():
    day = datetime.today().day
    return day


def get_data():
    day = get_day()
    cookie = get_session_cookie()
    response = requests.get(f"https://adventofcode.com/2022/day/{day}/input", cookies=cookie)
    print(response)

    return response.content


def write_data():

    day = get_day()
    content = get_data()
    filename = f"22/data/day_{day}.txt"

    with open(filename, "wb") as f:
        f.write(content)


if __name__ == "__main__":
    write_data()
