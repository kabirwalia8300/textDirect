from flask import Flask, request
from twilio.twiml.messaging_response import Message, MessagingResponse
import direct
import os
import re

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
api_key=os.getenv('API_KEY')

@app.route('/sms', methods=['GET','POST'])
def sms():

    querry_message = request.form['Body']
    assert querry_message.count(' ')==1
    index=querry_message.find(' ')
    start=querry_message[:index]
    end=querry_message[index+1:]

    directions = direct.sendInstructions(start, end, api_key)
    resp = MessagingResponse()
    isMultiple=False

    result = 'Hello! Here are your directions: '
    for x in range(len(directions)):
        result = result + '\n' + '#' + cleanhtml(directions[x])
        if len(result)>1560:
            isMultiple=True
            pos = result.rfind('#',0,1561)
            text = result[0:pos]
            resp.message(text)
            result= result[pos:]

    if not isMultiple:
        resp.message(result)

    return str(resp)

def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port, debug=True)


# send multiple text messages when character limit exceeded
