from typing import List, Optional
from datetime import datetime
import time
from plyer import notification
import json
import yaml
from beepy import beep

from cowinapi import CoWinAPI, VaccinationCenter, CoWinTooManyRequests

CoWinAPIObj = CoWinAPI()


# def get_available_centers_by_pin(pincode: str) -> List[VaccinationCenter]:
#     vaccination_centers = CoWinAPIObj.calendar_by_pin(pincode, CoWinAPI.today())
#     if vaccination_centers:
#         vaccination_centers = [vc for vc in vaccination_centers if vc.has_available_sessions()]
#     return vaccination_centers

def get_available_centers_by_pin(pincode: str) -> List[VaccinationCenter]:
    vaccination_centers = []
    try:
        vaccination_centers = CoWinAPIObj.calendar_by_pin(pincode, CoWinAPI.today())
    except Exception as e:
        print(e)
        pass
    return vaccination_centers


def notify(msg):
    title = 'SLOT OPEN'
    message = msg
    notification.notify(title = title,
                        message = message,
                        app_icon = None,
                        timeout = 50) 
    beep(sound=1)
    return


if __name__ == "__main__":

    # defaults
    pincode_list = []
    min_age_limit = 18

    with open(r'config.yaml') as file:
        # The FullLoader parameter handles the conversion from YAML
        # scalar values to Python the dictionary format
        documents = yaml.load(file, Loader=yaml.FullLoader)
        for item, doc in documents.items():
            if item == "pincode_list":
                pincode_list = doc
            if item == "min_age_limit":
                min_age_limit = doc
            if item == "vaccine_type":
                vaccine_type_list = doc



    while True:
        for pin in pincode_list:
            vaccination_centers = get_available_centers_by_pin(pin)
            if vaccination_centers is not None:
                for vc in vaccination_centers:
                    msg = "{}".format(vc)
                    session_list = vc.get_available_sessions_by_age_limit(min_age_limit)
                    msg2 = ""
                    for s in session_list:
                        if s.vaccine in vaccine_type_list and s.capacity > 0:
                            msg2 += "\ndate:{}\tvaccine:{}\tcapacity:{}".format(s.date, s.vaccine, s.capacity)
                    msg += "{}\n".format(msg2)
                    if msg2 != "":
                        print(msg)
                        notify(msg)
        
        time.sleep(10)


