import os
import re
import gmplot

def traceroute(address):
    print("Starting traceroute...")
    raw = os.popen("tracert "+address).read()
    addresses = []

    #Regex that finds all the IP addresses in tracert's output
    for add in re.findall(r"((\d{1,3}\.){3}\d)", raw):
        addresses.append(add[0])

    #Removes the target's and router's IP addresses
    addresses.pop(0)
    addresses.pop(0)

    return addresses

def getLocation(address, handler):
    #just send me location
    try:
        #gets the location of the ip address using ipinfo's api and returns coordinates as floats
        loc_raw = handler.getDetails(ip_address=address).loc.split(',')
        return float(loc_raw[0]), float(loc_raw[1])

    except AttributeError:
        #returns 0 on failure, happens when trying to locate 10.x.x.x addresses
        return 0

def mapDrawer(plotter, loc_list, outfile, u_loc):
    path = zip(*loc_list)
    plotter.plot(*path, edge_width=2, color='#00FF00')
    plotter.marker(u_loc[0], u_loc[1], color='red',title='You')
    plotter.marker(loc_list[-1][0], loc_list[-1][1], color='blue', title='endpoint')
    plotter.draw(outfile)
    print(f"Map successfully drawn on {outfile}")