"""import direct
message_body="Toronto Montreal"
index=message_body.find(' ')
start=message_body[:index]
end=message_body[index+1:]
print(start)
print(end)

directions = direct.sendInstructions(start, end)
result = 'Hello! Here are your directions: '
for x in range(len(directions)):
    result = result + '\n' + str(x+1) + '. ' + directions[x]

print(result)
"""

"""
from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
import direct

app = Flask(__name__)


@app.route('/sms', methods=['GET','POST'])
def sms():
    #number = request.form['FromCountry']
    #message_body = request.form['Body']

    resp = MessagingResponse()
    #resp.message('Hello {}, you said: {}'.format(number, message_body))
    resp.message('Hello')
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)"""


"""
origin = input('where are you: ').replace(' ','+')
destination = input('where do you want to go: ').replace(' ','+')
nav_request = 'origin={}&destination={}&key={}'.format(origin, destination, api_key)

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

print(instructions)"""
