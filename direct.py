import urllib.request
import json
import re

endpoint = 'https://maps.googleapis.com/maps/api/directions/json?'

def sendInstructions(origin, destination, api_key):

    orig = origin.replace(' ','+')
    dest = destination.replace(' ','+')
    nav_request = 'origin={}&destination={}&key={}'.format(orig, dest, api_key)
    request = endpoint+nav_request
    response = urllib.request.urlopen(request).read()
    directions=  json.loads(response)
    #print(directions)
    #routes = directions['routes']
    #legs = routes[0]['legs']
    #steps= legs[0]['steps']
    steps = directions['routes'][0]['legs'][0]['steps']
    instructions = []
    for x in steps:
        instructions.append(x['html_instructions'])

    return instructions

def printInstructions():
    start = input('where are you: ').replace(' ','+')
    end = input('where do you want to go: ').replace(' ','+')
    api_key= input('key: ').replace(' ','+')
    directions = sendInstructions(start, end, api_key)
    result = 'Hello! Here are your directions: '
    for x in range(len(directions)):
        result = result + '\n' + str(x+1) + '. ' + directions[x]
    print(result)

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

def charCount():
    start = input('where are you: ').replace(' ','+')
    end = input('where do you want to go: ').replace(' ','+')
    api_key= input('key: ').replace(' ','+')
    directions = sendInstructions(start, end, api_key)

    isMultiple=False
    output=[]
    result = 'Hello! Here are your directions: '
    for x in range(len(directions)):
        result = result + '\n' + '#' + cleanhtml(directions[x])
        if len(result)>1600:
            isMultiple=True
            pos = result.rfind('#',0,1601)
            text = result[0:pos]
            output.append(text)
            result= result[pos:]

    if not isMultiple:
        output.append(result)

    return output

if __name__=="__main__":
    printInstructions()
