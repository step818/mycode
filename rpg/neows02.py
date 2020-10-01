#!/usr/bin/python3
import requests

## Define NEOW URL 
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"


def main():
    ## first I want to grab my credentials
    with open("/home/student/pyapi/nasa/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")        

    ## update the date below, if you like
    startdate = "start_date=2020-10-07"
    enddate = "end_date=2020-10-07"
    ## the value below is not being used in this
    ## version of the script
    # enddate = "end_date=END_DATE"

    # make a request with the request library
    neowrequest = requests.get(NEOURL + startdate + "&"+ enddate + "&" +  nasacreds)

    # strip off json attachment from our response
    neodata = neowrequest.json()


    # make a list of dates to reference the list of near earth objects that day
    dates = []
    # for each element in the date's list, get the data for each near earth object
    for dat in neodata["near_earth_objects"]:
        dates.append(dat)
    print("\n")
    print(f"!*!*!*!  Near Earth Objects approching on {startdate}  !*!*!*!\n")   
    for y in dates:
        for x in neodata["near_earth_objects"][y]:
            print(f"Asteroid Name: \'{x['name']}\'\n Potentially Hazardous?? {x['is_potentially_hazardous_asteroid']}")
            for z in x["close_approach_data"]:
                print(f"{round(float(z['miss_distance']['kilometers']),0)} kilometers at closest approach\n")
                print("====================================================")

if __name__ == "__main__":
    main()

