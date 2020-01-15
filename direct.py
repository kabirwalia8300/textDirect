import urllib.request
import json

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = ''


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

def printInstructions():
    start = input('where are you: ').replace(' ','+')
    end = input('where do you want to go: ').replace(' ','+')
    directions = sendInstructions(start, end)
    result = 'Hello! Here are your directions: '
    for x in range(len(directions)):
        result = result + '\n' + str(x+1) + '. ' + directions[x]
    print(result)

if __name__=="__main__":
    printInstructions()
