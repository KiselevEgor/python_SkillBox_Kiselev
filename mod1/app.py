from flask import Flask
import datetime
import random
import os
import re

app = Flask(__name__)

cars = ["Chevrolet", "Renault", "Ford", "Lada"]
cats = ['орниш-рекс','русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']

@app.route('/hello_world')
def hello_world():
    return 'Привет, мир!'

@app.route('/cars')
def get_cars():
    return ', '.join(cars)

@app.route('/cats')
def get_cats():
    return random.choice(cats)

@app.route('/get_time/now')
def get_time_now():
    current_time = datetime.datetime.now()
    return f"Точное время: {current_time}"

@app.route('/get_time/future')
def get_time_future():
    current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
    return f"Точное время через час будет {current_time_after_hour}"


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
BOOK_FILE = os.path.join(BASE_DIR, 'war_and_peace.txt')

def get_words_from_book():
    with open(BOOK_FILE, 'r') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text)
        return words

words_list = get_words_from_book()

@app.route('/get_random_word')
def get_random_word():
    random_word = random.choice(words_list)
    return random_word

count = 0

@app.route('/counter')
def get_count():
    global count
    count += 1
    return str(count)


if __name__ == '__main__':
    app.run()