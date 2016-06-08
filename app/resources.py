from flask_restful import Resource, fields, abort, marshal_with, reqparse
from models import Drone

drone_fields = {
    'drone_id': fields.String,
    'status': fields.String,
    'device_id': fields.String,
    'mac': fields.String,
    'channel': fields.String,
    'client_mac': fields.String
}


class DroneAPI(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('status', type=str, required=True, help='No status provided', location='json')
        self.parser.add_argument('device_id', type=str, required=True, help='No device_id provided', location='json')
        self.parser.add_argument('mac', type=str, required=True, help='No mac provided', location='json')
        self.parser.add_argument('channel', type=str, required=True, help='No channel provided', location='json')
        self.parser.add_argument('client_mac', type=str, required=True, help='No client_mac provided', location='json')
        super(DroneAPI, self).__init__()

    @marshal_with(drone_fields, envelope='drone')
    def get(self, drone_id):
        drone = Drone.get(drone_id)
        if drone is None:
            abort(404)

        return drone

    @marshal_with(drone_fields, envelope='drone')
    def put(self, drone_id):
        args = self.parser.parse_args()

        drone = Drone.get(drone_id)
        if drone is None:
            drone = Drone(drone_id)

        drone.status = args['status']
        drone.device_id = args['device_id']
        drone.mac = args['mac']
        drone.channel = args['channel']
        drone.client_mac = args['client_mac']
        drone.persist()

        return drone

    def delete(self, drone_id):
        success = Drone.delete_by_id(drone_id)
        if not success:
            abort(404)

        return {'result': True}
