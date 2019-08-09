import subprocess
import time
from subprocess import PIPE
from sys import platform
import datetime

def get_packageloss(input):
    packetloss = float(
        [x for x in input.split('\n') if x.find('packet loss') != -1][0].split('%')[0].split(' ')[-1])
    return packetloss


def get_responsetime(input):
    responsetime = -20
    for x in input.split('\n'):
        if platform == 'linux':
            if x.find('rtt min/avg/max/mdev') != -1:
                responsetime = float(x.split('=')[1].split('/')[1])
        elif platform == 'darwin':
            if x.find('round-trip min/avg/max/stddev') != -1:
                responsetime = float(x.split('=')[1].split('/')[1])
        else:
            responsetime = -20
    return responsetime


def note_to_file(input):
    filename=datetime.datetime.now().strftime("record_%Y-%m-%d.txt")
    with open(filename, 'a+') as file:
        file.write(input)


if __name__ == '__main__':
    hostname = "8.8.8.8"
    while (True):
        process = subprocess.Popen(['ping', '-c', '3', hostname],
                                   stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        input = stdout.decode('utf-8')

        now = time.mktime(time.localtime())
        packetloss = get_packageloss(input)
        responsetime = get_responsetime(input)

        note_to_file("{} {} {}\n".format(packetloss, responsetime, now))
        print("Package Loss: {} % \t Response Time: {} ms \t Time: {}".format(packetloss, responsetime, now))
