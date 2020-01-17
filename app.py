from flask import Flask, request, session
from twilio.twiml.messaging_response import Message, MessagingResponse
import direct
import os
import re

SECRET_KEY = 'tester'
app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))
api_key=os.getenv('API_KEY')
app.config.from_object(__name__)

@app.route('/sms', methods=['GET','POST'])
def sms():
    counter = session.get('counter', 0)
    counter += 1
    # Save the new counter value in the session
    session['counter'] = counter
    resp = MessagingResponse()
    querry_message = request.form['Body']

    if querry_message.strip().casefold()=='textdirect':
        resp.message('Hello! Welcome to textDirect!'+' Please use the following '
        +'format to send your request: address of origin*address of destination*'
        +'language*mode of transport')
        return str(resp)

    else:
        try:
            querry_message.strip()
            length = len(querry_message)
            assert querry_message.count('*')==3
            ind_1=querry_message.index('*')
            start=querry_message[:ind_1]
            ind_2=querry_message.index('*',ind_1+1, length)
            end=querry_message[ind_1+1:ind_2]
            ind_3=querry_message.index('*',ind_2+1, length)
            lang=querry_message[ind_2+1:ind_3]
            travelMode=querry_message[ind_3+1: length]

            directions = direct.sendInstructions(start, end, api_key, lang, travelMode)
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

        except:
            resp.message('Incorrect format')
            return str(resp)


def cleanhtml(raw_html):
  cleanr = re.compile('<.*?>')
  cleantext = re.sub(cleanr, '', raw_html)
  return cleantext

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=port, debug=True)
