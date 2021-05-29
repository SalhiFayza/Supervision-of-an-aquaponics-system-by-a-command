
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime
import numpy as np
from datetime import datetime

current_date_and_time = datetime.today().strftime('%Y-%m-%d')
current_date_and_time_string = str(current_date_and_time)
file_name = current_date_and_time_string + ".csv"


I020 = [ line.strip('\n').split(",") for line in open(file_name)][1:]
Time = [datetime.strptime(line[1],"%H:%M:%S") for line in I020]
Time1 = [mdates.date2num(line) for line in Time]
Solar = [float(line[3]) for line in I020]

xs = np.array(Time1)  # You don't really need to do this but I've left it in
ys = np.array(Solar)

fig, ax = plt.subplots() # using matplotlib's Object Oriented API

ax.set_title('Solar data')
ax.set_xlabel('Time')
ax.set_ylabel('Solar')
ax.plot_date(xs, ys, 'k-')

hfmt = mdates.DateFormatter('%H:%M:%S')
ax.xaxis.set_major_formatter(hfmt)
plt.gcf().autofmt_xdate()

plt.show()