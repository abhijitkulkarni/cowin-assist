# cowin-assist
A python script to search for open slots for covid-19 vaccination. It will generate desktop notifications. Upon receiving the notification, the user will need to do the registration manually.

## Install
Create a python virtual environment. Install the packages with following command
`pip install -r requirements.txt`

## Configuration
To configure the settings, edit the config.yaml file. You can edit min_age_limit (18/45), vaccine_type (COVAXIN/COVISHIELD) and pincode entries where you want to search the appointment for.

## Run
To run the sctipt from virtual environment run on command shell - 
`python cowinmain.py`

The script will look for open slots every 10 secs, and update notifications on desktop.

## Note
This is the basic version created in a day and run on a Linux laptop only. It may run as is on Windows machine but I haven't tested it. You may modify it as it suits you.
