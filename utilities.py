import os
import re
import ipinfo


def traceroute(address):
    print("starting traceroute")
    raw = os.popen("tracert "+address).read()
    #print(raw)
    addresses = []
    for add in re.findall(r"((\d{1,3}\.){3}\d)", raw):
        addresses.append(add[0])

    #the target address
    #t_address = addresses[0]
    addresses.pop(0)
    addresses.pop(0)

    return addresses

def getLocation(address, handler):
    #just send me location
    try:
        loc_raw = handler.getDetails(ip_address=address).loc.split(',')
        return float(loc_raw[0]), float(loc_raw[1])
    except AttributeError:
        #print(f"failed to get location for {0}".format(address))
        return 0

if __name__=="__main__":
    for i in traceroute("facebook.com"):
        print(f"{i}: {getLocation(i,handle)}")