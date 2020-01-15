from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
import direct
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
api_key=os.getenv('API_KEY')

@app.route('/sms', methods=['GET','POST'])
def sms():

    message_body = request.form['Body']
    assert message_body.count(' ')==1
    index=message_body.find(' ')
    start=message_body[:index]
    end=message_body[index+1:]

    directions = direct.sendInstructions(start, end, api_key)
    result = 'Hello! Here are your directions: '
    for x in range(len(directions)):
        result = result + '\n' + str(x+1) + '. ' + remove_tags(directions[x])


    resp = MessagingResponse()

    resp.message(result)
    return str(resp)

def remove_tags(text):
    return ''.join(xml.etree.ElementTree.fromstring(text).itertext())

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port, debug=True)

#see how to clean html
# send multiple text messages when character limit exceeded
