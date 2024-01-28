import requests
import urllib3
import polyline
import gmplot

urllib3.disable_warnings()


###############################
##  Getting the Strava Data  ##
###############################
def getPlotData(city, activity_type, per_page_requests):
    #Desired filters
    desired_city = city
    desired_activity_type = activity_type


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
    per_page = per_page_requests
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



    #Format the plotting data by individual rides
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

    return individual_polyline_return_data


#########################
##  Plotting the data  ##
#########################


#Google API stuff
apikey = 'AIzaSyDHVH624Z46hGWgh3PZNMQ8CmKF91CJkdE' # (your API key here)

#Get the strava data using getStravaData
city_to_plot = "Napa"
activity_to_plot = "Run"
total_route_data = getPlotData(city_to_plot, activity_to_plot, 353)

#Centering coordinates
if city_to_plot == "PTown":
    coord_lat = 41.68569
    coord_long = -73.89769
elif city_to_plot == "Napa":
    coord_lat = 38.29535
    coord_long = -122.29778

gmap = gmplot.GoogleMapPlotter(coord_lat, coord_long, 14, apikey=apikey)


# Outline the runs
for element in total_route_data:
    run_outline = zip(*element)
    gmap.polygon(*run_outline, color='cornflowerblue', edge_width=2, face_color="FFC0CB", face_alpha=0)

# Draw the map to an HTML file:
gmap.draw('index.html')

print(f"Map drawn with {activity_to_plot} activities from {city_to_plot}")
print("\nWebsite will update shortly...")


'''
add all the routes together, like the convex hull problem, and see how much area of the united states youve run through
'''

#NOTE the problem is that its makign a polygon, i have to plot the route, then plot the reverse route so that it doesn't have that line down the middle