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


def get_data(day: int):
    cookie = get_session_cookie()
    response = requests.get(f"https://adventofcode.com/2021/day/{day}/input", cookies=cookie)
    print(response)

    return response.content


def write_data():

    day = 3
    content = get_data(day)
    filename = f"21/data/day_{day}.txt"

    with open(filename, "wb") as f:
        f.write(content)


if __name__ == "__main__":
    write_data()
