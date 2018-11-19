## Simple Twilio Texting App

Procedure
1. Create a Twilio Account
2. Obtain your Twilio Credentials (account SID and auth token)
![Twilio Credentials](https://github.com/eukolyptus/Simple-Twilio-Texting-App/blob/master/imgs/twilioCredentials.png?raw=true)

3. Add a phone number on Twilio that you can recieve texts on (https://www.twilio.com/console/phone-numbers/verified)
![Verify Phone](https://github.com/eukolyptus/Simple-Twilio-Texting-App/blob/master/imgs/verifyPhone.png?raw=true)

4. Get your Twilio phone number (https://www.twilio.com/console/phone-numbers/incoming)
![Twilio Phone Number](https://github.com/eukolyptus/Simple-Twilio-Texting-App/blob/master/imgs/twilioPhone.png?raw=true)

5. Open up an IDE (I am using PyCharm)
6. Download the Twilio Python Helper library (on PyCharm, you can download this library in the Project Interpreter preferences)
7. Modify credentials.py with the account SID, auth token, your phone number, and your Twilio phone number
8. Run send_sms.py to send an SMS from your Twilio phone number to your personal phone
