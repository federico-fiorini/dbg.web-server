from flask import render_template
from app import app
from app.models import Device
from app import api
from resources import DroneAPI

@app.route("/")
def index():
    return render_template('index.html', title='Logs')

@app.route("/map")
def map():

    devices = Device.get_all()
    list = [{'lat': device.lat, 'lng': device.lng} for device in devices]
    return render_template('map.html', title='Map', devices=list)


api.add_resource(DroneAPI, '/drone/<string:drone_id>', endpoint='drone')