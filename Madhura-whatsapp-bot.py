pip install adafruit-io
import os
x = os.getenv('x')  #ADAFRUIT_IO_USERNAME
y = os.getenv('y')   #ADAFRUIT_IO_KEY

from Adafruit_IO import Client, Feed
aio = Client(x,y)

# create a feed 
feed = Feed(name='wbot')#Feed name is given
result = aio.create_feed(feed)
result

from Adafruit_IO import Data # data is actually a method from adafruit library
#sending the value to a feed
value = Data(value=0)
data_send = aio.create_data('wbot', value)

pip install twilio
import os
from twilio.rest import Client 

account_sid = os.getenv('account_sid')
auth_token = os.getenv('auth_token')
client = Client(account_sid, auth_token)

from_whastapp_number = 'whatsapp:+14155238886'
to_whastapp_number = 'whatsapp:+919325583070'

message = client.messages \
    .create(
         media_url=['https://i.pinimg.com/originals/98/26/86/982686f070e5c77b64a71f83a96b7167.jpg'],
         from_='whatsapp:+14155238886',
         body="Light ON!!",
         to='whatsapp:+919325583070'
     )
print(message.sid)
message = client.messages \
    .create(
         media_url=['http://i.xp.io/2L3jia5T.png'],
         from_='whatsapp:+14155238886',
         body="Light OFF!!",
         to='whatsapp:+919325583070'
     )
print(message.sid)
  
