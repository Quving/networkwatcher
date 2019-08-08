import datetime

import matplotlib.dates as md
import matplotlib.pyplot as plt
import numpy as np


def get_values():
    with open("notes.txt", 'r') as file:
        data = file.read()

    data = [[float(y) for y in x.split()] for x in data.split('\n') if x]

    # print([list(t) for t in zip(*data)])
    packageloss, reponsetime, time = zip(*data)

    return [[packageloss, reponsetime], np.array(time)]


def plot(x, y1, y2):
    plt.title('Beehive Network Monitor')

    plot1 = plt.subplot(211)
    # plt.subplots_adjust(bottom=0.5)
    plt.xticks(rotation=90)
    ax = plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d %H:%M:%S')
    ax.xaxis.set_major_formatter(xfmt)
    plt.ylabel('Package Loss (%)')
    plt.plot(x, y1, '.-')

    plot2 = plt.subplot(212)
    ax = plt.gca()
    ax.xaxis.set_major_formatter(xfmt)
    plt.xticks(rotation=90)
    plot2.plot(x, y2, '.-')
    plt.ylabel('Response Time (ms)')
    plt.xlabel('timestamp')
    plot1.set_xticklabels([])
    plot1.get_shared_x_axes().join(plot1, plot2)

    plt.autoscale()
    plt.show()


if __name__ == '__main__':
    vals = get_values()
    time = vals[1]

    dates = [datetime.datetime.fromtimestamp(ts) for ts in vals[1]]
    datenums = md.date2num(dates)
    plot(x=datenums, y1=vals[0][0], y2=vals[0][1])
