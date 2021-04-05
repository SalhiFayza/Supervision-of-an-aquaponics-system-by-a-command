from datetime import datetime
import pandas as pd
import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content

current_date_and_time = datetime.today().strftime('%Y-%m-%d')
current_date_and_time_string = str(current_date_and_time)
file_name = current_date_and_time_string + ".csv"

 
def read():
    df = pd.read_csv(file_name)
    minValueOfTemperature = df.query('Temperature == Temperature.max()')
    maxvalueOFTemperature = df.query('Temperature == Temperature.min()')
    minValueOfHumidity = df.query('Humidity == Humidity.max()')
    maxvalueOFHumidity = df.query('Humidity == Humidity.min()')
    print("===========Max Value Of Temperature ===========")
    print(minValueOfTemperature)
    print("===========Min Value Of Temperature ===========")
    print(maxvalueOFTemperature)
    print("===========Max Value Of Humidity ===========")
    print(minValueOfHumidity)
    print("===========Min Value Of Humidity ===========")
    print(maxvalueOFHumidity)
    information ='Min Value Of Temperature \n' + str(minValueOfTemperature) + 'Max Value Of Temperature \n' + str(maxvalueOFTemperature) + 'Min Value Of Humidity \n' + str(minValueOfHumidity) + 'Max Value Of Humidity \n' + str(maxvalueOFHumidity)
    try:
        # hadha api sendgrid yab3thw bih emails //
        sg = sendgrid.SendGridAPIClient(api_key="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")
        from_email = Email("fayzasalhi2021@gmail.com")  # Change to your verified sender
        to_email = To("Benlassouedfarah@gmail.com")  # Change to your recipient
        subject = "Rapport Of {} ".format(current_date_and_time)
        content = Content("text/plain", "Rapport {0} ".format(information))
        mail = Mail(from_email, to_email, subject, content)

        # Get a JSON-ready representation of the Mail object
        mail_json = mail.get()

        # Send an HTTP POST request to /mail/send
        response = sg.client.mail.send.post(request_body=mail_json)
        print("done sending Rapport")
    except:
        print('SMTP NOT WORK  ')
read()