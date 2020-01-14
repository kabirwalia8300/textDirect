import urllib.request
import json

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'AIzaSyCykBl-DK7iqVeUVtSQrvs2Ggxv_HnPmKA'


def sendInstructions(origin, destination):

    orig = origin.replace(' ','+')
    dest = destination.replace(' ','+')
    nav_request = 'origin={}&destination={}&key={}'.format(orig, dest, api_key)
    request = endpoint+nav_request
    response = urllib.request.urlopen(request).read()
    directions=  json.loads(response)
    #print(directions)
    routes = directions['routes']
    legs = routes[0]['legs']
    steps= legs[0]['steps']
    length = len(steps)
    instructions = []
    for x in steps:
        instructions.append(x['html_instructions'])

    return instructions

def printInstructions(orig,des):
    print(sendInstructions(orig, des ))

if __name__=="__main__":
    printInstructions(orig,des)
