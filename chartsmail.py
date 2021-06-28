import plotly
import plotly.graph_objs as go
from datetime import datetime
import smtplib
import cufflinks as cf
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
# since i'm geek and lazy i want to make ur life easy too so i get username of windows directly
#bref any problem contact me
import os
username = os.getlogin()

current_date_and_time = datetime.datetime.now().strftime('%Y-%m-%d')
current_date_and_time_string = str(current_date_and_time)
file_name = current_date_and_time_string + ".csv"


def read():
    I020 = [line.strip('\n').split(",") for line in open(file_name)][1:]

    Time = [datetime.datetime.strptime(line[1], "%H:%M:%S") for line in I020]

    temp = [float(line[3]) for line in I020]
    humy = [float(line[2]) for line in I020]
    Water = [float(line[4]) for line in I020]
    ph = [float(line[5]) for line in I020]

    random_x = Time
    random_y0 = temp
    random_y1 = humy
    random_y2 = Water
    random_y3 = ph

    trace0 = go.Scatter(
        x=random_x,
        y=random_y0,
        mode='lines',
        name='Temp(°C)'

    )

    trace1 = go.Scatter(
        x=random_x,
        y=random_y1,
        mode='lines',
        name='Humidity(%)'

    )

    trace2 = go.Scatter(
        x=random_x,
        y=random_y2,
        mode='lines',
        name='WaterTemp(°C)'
    )

    trace3 = go.Scatter(
        x=random_x,
        y=random_y3,
        mode='lines',
        name='pH'
    )
    # Structure traces as datasets
    data1 = [trace0]
    data2 = [trace1]
    data3 = [trace2]
    data4 = [trace3]

    # Build figures
    fig1 = go.Figure(data=data1)
    fig2 = go.Figure(data=data2)
    fig3 = go.Figure(data=data3)
    fig4 = go.Figure(data=data4)
    figs = cf.subplots([fig1, fig2, fig3, fig4], shape=(2, 2))
    figs['layout'].update(height=630, width=1350, title='Data For Aquaponics')
    plotly.offline.plot(figs,
                        filename='C:/Users/'+username+'/Desktop/update.html', show_link=False)
    try:
        sender_address = 'farahbenlassoued1@gmail.com'
        sender_pass = 'farahtaz2020'
        receiver_address = 'fayzasalhif@gmail.com'

        msg = MIMEMultipart()

        msg['From'] = sender_address
        msg['To'] = receiver_address
        msg['Subject'] = "Rapport Of {} ".format(current_date_and_time)
        body = "Good Morning Sir."
        msg.attach(MIMEText(body, 'plain'))

        # open the file to be sent
        filename = "Update OF Courbes.html"
        attachment = open("C:/Users/"+username+"/Desktop/update.html", "rb")

        p = MIMEBase('application', 'octet-stream')

        p.set_payload((attachment).read())

        encoders.encode_base64(p)

        p.add_header('Content-Disposition', "attachment; filename= %s" % filename)
        msg.attach(p)
        # Create SMTP session for sending the mail
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_address, sender_pass)  # login with mail_id and password
        text = msg.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')
    except:
        print("Smtp Have Problem")

read()
