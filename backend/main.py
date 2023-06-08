# pip3 install flask
import datetime

from flask import Flask

app = Flask('avi_app')  # create flask instance


@app.route('/welcome')
def welcome_page():
    return f'welcome to out flask application {datetime.datetime.now()}'


app.run(port=5001)
