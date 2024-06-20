from flask import Flask, render_template
from datetime import datetime
import pytz

app = Flask(__name__)

# Get all timezones and their current time
def get_timezones():
    timezones = {}
    for tz in pytz.all_timezones:
        now = datetime.now(pytz.timezone(tz))
        timezones[tz] = now.strftime('%Y-%m-%d %H:%M:%S')
    return timezones

@app.route('/')
def home():
    timezones = get_timezones()
    return render_template('index.html', timezones=timezones)

if __name__ == '__main__':
    app.run(debug=True)
