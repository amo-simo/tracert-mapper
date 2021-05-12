import ipinfo
from utilities import traceroute, getLocation, mapDrawer
import sys
import gmplot

try:
    t_address = sys.argv[1]
except IndexError:
    t_address = input("Please specify the address: ")


IPINFO_API_KEY= '' #your ipinfo api key
handle = ipinfo.getHandler(IPINFO_API_KEY)

#get the user's location to center the map
u_loc = getLocation(None, handle)

google_api_key = '' #your google maps api key (optional)
gmap = gmplot.GoogleMapPlotter(u_loc[0], u_loc[1], 0,apikey=google_api_key)

#get the traceroute addresses and initialize the coordinates list
addresses = traceroute(t_address)
locations = []

for address in addresses:
    loc = getLocation(address, handle)
    if loc != 0:
        locations.append(loc)
    else: pass

mapDrawer(gmap, locations, "map.html", u_loc)

