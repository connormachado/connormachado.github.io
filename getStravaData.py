import requests
import urllib3
import polyline

urllib3.disable_warnings()

#Variables for filtering
desired_city = "Napa"
desired_activity_type = "Run"


#Strava API crap
auth_url = "https://www.strava.com/oauth/token"
activites_url = "https://www.strava.com/api/v3/athlete/activities"

payload = {
    'client_id': "64277",
    'client_secret': 'bfbb04dd08e0ea9abc94a41763c3e61b5cac9a7e',
    'refresh_token': 'd41b9d0094cd50208d1b4160b0f677cc92650060',
    'grant_type': "refresh_token",
    'f': 'json'
}

print("Requesting Token...\n")
res = requests.post(auth_url, data=payload, verify=False)
access_token = res.json()['access_token']
# print("Access Token = {}\n".format(access_token) + "\n")


#How many activities we want
per_page = 353
is_large_set = False
header = {'Authorization': 'Bearer ' + access_token}


#If there are too many activities to do at once
if per_page > 30:
    #Full set
    large_data_set = []
    curr_page = 1
    
    while(True):
        print(f"Iteration {curr_page} with 30 activities each...")
        #Repeat until no more activities
        if per_page > 30:
            param = {'per_page': 30, 'page': curr_page}

            my_dataset = requests.get(activites_url, headers=header, params=param).json()
            
            #Add all activities to the large dataset
            for new_activity in my_dataset:
                large_data_set.append(new_activity)

            curr_page += 1
            per_page -= 30
        else:
            param = {'per_page': per_page, 'page': curr_page}

            my_dataset = requests.get(activites_url, headers=header, params=param).json()
            
            for new_activity in my_dataset:
                large_data_set.append(new_activity)
            
            is_large_set = True
            break

    print("Large data set compiled with length " + str(len(large_data_set)))


#If dataset can be obtained using 1 get request
else:
    print("Small data set recognized, one GET request needed...\n")
    param = {'per_page': per_page, 'page': 1}
    my_dataset = requests.get(activites_url, headers=header, params=param).json()
    print("Small data set compiled with length " + str(len(my_dataset)) + "\n")


#Merge large_data_set
if is_large_set:
    my_dataset = large_data_set


#Sort the activities by type
#NOTE this might be redundant because we have to filter the data again later
runActivities = []
rideActivities = []
otherTypeActivities = []

for activity in my_dataset:
    if "Run" in activity["type"]:
        runActivities.append(activity)
    elif "Ride" in activity["type"]:
        rideActivities.append(activity)
    else:
        otherTypeActivities.append(activity)

print("Runs: " + str(len(runActivities)) + "\nRides: " + str(len(rideActivities)) + "\nOthers: " + str(len(otherTypeActivities)))


#Sort the activities by location
napaActivities = []
pTownActivities = []
otherLocationActivities = []

for activity in my_dataset:
    if "Los_Angeles" in activity["timezone"]:
        napaActivities.append(activity)
    elif "New_York" in activity["timezone"]:
        pTownActivities.append(activity)
    else:
        otherLocationActivities.append(activity)

print( "\nNapa Activities: " + str(len(napaActivities)) 
      +"\nPoughkeepsie Activities: " + str(len(pTownActivities)) 
      +"\nOther Places: " + str(len(otherLocationActivities)))

print("-------------------------------------------------------------------")

#Sort activities by given filters (city and activity type)
filtered_return_list = []
city_data = []

#Add desired city data
if "PTown" == desired_city:
    city_data = city_data + pTownActivities
elif "Napa" == desired_city:
    city_data = city_data + napaActivities
else:
    city_data = city_data + otherLocationActivities

#Add desired activity type data 
for element in city_data:
    if ("Run" == element["type"]) and ("Run" == desired_activity_type):
        filtered_return_list.append(element)
    elif ("Ride" == element["type"]) and ("Ride" == desired_activity_type):
        filtered_return_list.append(element)
    elif "Other" == desired_activity_type:
        filtered_return_list.append(element)

for element in filtered_return_list:
    print(element["name"])
    print(element["start_date"])
    print("\n")


# Get plot data
#NOTE get individual routes in order to plot better
#NOTE the plotting will allow the routes to not be messed up
#NOTE you can also see the roads better probably
individual_polyline_return_data = []

for activity in filtered_return_list:
    new_route = []

    summary_polyline = activity["map"]["summary_polyline"]

    coordinates = polyline.decode(summary_polyline)

    ride_latitudes = [coordinate[0] for coordinate in coordinates] #Lat
    ride_longitudes = [coordinate[1] for coordinate in coordinates] #Long

    for element in range(len(ride_longitudes)):
        new_route.append( (ride_latitudes[element], ride_longitudes[element]) )
    
    #Gets rid of the line b/c it plots a polygon not a line shape
    new_route_temp = new_route.copy()
    new_route_temp.reverse()
    new_route += new_route_temp
    
    individual_polyline_return_data.append(new_route)

print(individual_polyline_return_data)