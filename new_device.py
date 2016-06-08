from app.models import Device

lat = raw_input("Please enter latitude: ")
lng = raw_input("Please enter longitude: ")

device = Device(lat, lng)
device.persist()
