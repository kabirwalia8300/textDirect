# we import the Twilio client from the dependency we just installed
import twilio
from twilio.rest import Client
# the following line needs your Twilio Account SID and Auth Token
client = Client('ACaa0eac6d1add52d9702a4c2130d2d084','3678b1cd842cddf0eb79af466486d1ef')
# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
# aarushi number
client.messages.create(to="+919820208300",
                       from_="+12564884302",
                       body="Hola! Que pa so senorita! Say hi to your fat boyfriend.")
