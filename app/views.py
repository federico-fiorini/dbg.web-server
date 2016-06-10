from flask import render_template
from app import app
from app.models import Device, Drone
from app import api
from resources import DroneAPI

@app.route("/")
def index():
    drones = Drone.get_all()
    list = [{'status': drone.status, 'device': drone.device_id,
            'drone_id': drone.drone_id, 'mac': drone.mac} for drone in drones]
    return render_template('index.html', title='Logs', drones=list)

@app.route("/map")
def map():

    devices = Device.get_all()
    list = [{'lat': device.lat, 'lng': device.lng} for device in devices]
    return render_template('map.html', title='Map', devices=list)


api.add_resource(DroneAPI, '/drone/<string:drone_id>', endpoint='drone')