##DRONE BE GONE - WEB SERVER

###HOW TO SET UP

    # Create python virtualenv
    virtualenv .env

    # Install required dependencies
    source .env/bin/activate
    pip install -r requirements.txt
    deactivate

    # Add devices to system
    python new_device.py

###HOW TO RUN

    # Run
    ./run.py

    # Go on localhost:5000
