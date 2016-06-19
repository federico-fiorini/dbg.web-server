##DRONE BE GONE - WEB SERVER
<br>
Drone Be Gone is a system that creates a no-fly zone where drones cannot enter. Currently works only with Parrot drones (controlled via wifi).

###HOW IT WORKS
The system works with a certain number of devices (we used Raspberry Pi) disposed on the perimeter of the designed no-fly zone and connected to a central web server that implements a simple REST API and shows logs informations. <br><br>
[Here](https://github.com/federico-fiorini/dbg.web-server) there is the implementation of the web server while on the devices we run the [client application](https://github.com/federico-fiorini/dbg.client).

###HOW TO SET UP

    # Create python virtualenv
    virtualenv .env

    # Install required dependencies
    source .env/bin/activate
    pip install -r requirements.txt
    deactivate

    # Add devices to system (not required for the system to work)
    python new_device.py

###HOW TO RUN

    # Run
    ./run.py

    # Go on localhost:5000
