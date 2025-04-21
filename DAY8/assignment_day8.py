from flask import Flask, request, jsonify
import random
import os
from datetime import datetime,timedelta
from random import choices
current_day = 'mon'

app = Flask(__name__)

def find_day(c_day):
    days = ['sun','mon','tue','wed','thu','fri','sat']
    current_day = c_day
    index = days.index(current_day)
    next_day = days[(index+1) % len(days)]
    return next_day

def find_date(i):
    start_date = datetime.today()
    current_date = start_date + timedelta(days = i)
    format_date = current_date.strftime('%D %B %Y')
    return format_date
    
def weather_data_generation(city):
    global current_day
    weather_dict = {}
    weather_dict['city'] = city
    weather_dict['pubDate'] = datetime.today()
    weather_dict['condition'] = dict(code = random.randint(20,50),date = datetime.today(),
    temperature = round(random.uniform(15.0,40.0),2),
    text = random.choice(['Mostly Cloudy','Cloudy','partly cloudy','Mostly sunny','Breeze','Clear']))
 
    no_of_times = 10
   
    weather_list = []
    for i in range(no_of_times):
        forecast_data = {
            'code': random.randint(20,50),
            'date': find_date(i),
            'day':find_day(current_day),
            'high': random.randint(25,49),
            'low': random.randint(10,20),
            'text':random.choice(['Mostly Cloudy','Cloudy','partly cloudy','Mostly sunny','Breeze','Clear'])
        }
        weather_list.append(forecast_data)
        current_day = find_day(current_day)
    weather_dict['forecast'] = weather_list
    return weather_dict
    
@app.route('/<string:city>',methods = ['Get'])
def weather(city):
    data = weather_data_generation(city)
    return jsonify(data)
   
if __name__  ==  '__main__':
    app.run()
