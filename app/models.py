from app import db
from sqlalchemy.exc import IntegrityError

class Drone(db.Model):

    __tablename__ = 'drones'

    drone_id = db.Column(db.String, primary_key=True)
    status = db.Column(db.String)
    device_id = db.Column(db.String)
    mac = db.Column(db.String)
    channel = db.Column(db.String)
    client_mac = db.Column(db.String)

    def __init__(self, id, status=None, device_id=None):
        self.drone_id = id
        self.status = status
        self.device_id = device_id

    @staticmethod
    def get(drone_id):
        return Drone.query.filter_by(drone_id=drone_id).first()

    def persist(self):
        try:
            db.session.add(self)
            db.session.commit()
            self.drone_id
        except IntegrityError:
            return False

        return True

    @staticmethod
    def delete_by_id(drone_id):
        drone = Drone.query.filter_by(drone_id=drone_id).first()
        if drone is None:
            return False

        db.session.delete(drone)
        db.session.commit()
        return True


class Device(db.Model):
    __tablename__ = 'devices'

    device_id = db.Column(db.String, primary_key=True)
    lat = db.Column(db.String, primary_key=True)
    lng = db.Column(db.String, primary_key=True)

    def __init__(self, lat, lng):
        self.lat = lat
        self.lng = lng

    def persist(self):
        try:
            db.session.add(self)
            db.session.commit()
        except IntegrityError:
            return False

        return True

    @staticmethod
    def get_all():
        return Device.query.all()
