from __future__ import with_statement
import contextlib
from urllib.request import urlopen
import sys
import bcolors,argparse
import requests
import os

def banner():
    print(bcolors.BLUE + """
        ██╗░░░██╗██████╗░██╗░░░░░░░░░░░███╗░░░███╗░█████╗░███╗░░██╗██╗██████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
        ██║░░░██║██╔══██╗██║░░░░░░░░░░░████╗░████║██╔══██╗████╗░██║██║██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
        ██║░░░██║██████╔╝██║░░░░░█████╗██╔████╔██║███████║██╔██╗██║██║██████╔╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
        ██║░░░██║██╔══██╗██║░░░░░╚════╝██║╚██╔╝██║██╔══██║██║╚████║██║██╔═══╝░██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
        ╚██████╔╝██║░░██║███████╗░░░░░░██║░╚═╝░██║██║░░██║██║░╚███║██║██║░░░░░╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
        ░╚═════╝░╚═╝░░╚═╝╚══════╝░░░░░░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝╚═╝░░░░░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝
                                                                                                                 Coded By: NG    
           """)
if len(sys.argv) > 1:
    banner()
    if (sys.argv[1] == '-s'):
            try:
                input_url = sys.argv[2]

                parser = argparse.ArgumentParser()
                parser.add_argument("-s", required=True)
                parser.add_argument("-help")
                args = parser.parse_args()

                if(os.path.isfile(input_url) == True):
                    with open(sys.argv[2], 'r') as f:
                        for line in f.readlines():
                            short_url = 'http://tinyurl.com/api-create.php?url=' + line
                            with contextlib.closing(urlopen(short_url)) as response:
                                print(bcolors.OKMSG + response.read().decode('utf-8'))
                else:
                    short_url = 'http://tinyurl.com/api-create.php?url=' + input_url
                    with contextlib.closing(urlopen(short_url)) as response:
                        print(bcolors.OKMSG + response.read().decode('utf-8'))

            except:
                banner()
                print(bcolors.ERR + 'Please enter python  url-manipulator.py -s <Required Path> ')

    elif (sys.argv[1] == '-f'):
          try:
                input_url_shortner = sys.argv[2]
                parser = argparse.ArgumentParser()
                parser.add_argument("-f", required=True)
                parser.add_argument("-help")
                args = parser.parse_args()

                if(os.path.isfile(input_url_shortner) == True):
                    with open(sys.argv[2], 'r') as f:
                        for line in f.readlines():
                            request_shortner = requests.get(line)
                            print(bcolors.OKMSG + request_shortner.url)
                else:
                    request_shortner = requests.get(input_url_shortner)
                    print(bcolors.OKMSG + request_shortner.url)
          except:
                banner()
                print(bcolors.ERR + 'Please enter python  url-manipulator.py -f <Required Path>')

    elif ((sys.argv[1] == '-h') | (sys.argv[1] == '--help')):
            print(bcolors.BOLD + 'usage: url-manipulator.py [-h] -d DOMAIN' '\n' 'OPTIONS:' '\n' '-h,--help    '
                             'show this help message and exit' '\n''-s Shortner,   --shorting the single url or location of file with multiple urls' '\n' '-f Full URL,    --Full URL or location of file with multiple urls')
else:
     banner()
     print(bcolors.ERR + 'Please select at least 1 option from (-s,-f) or -h, with a valid domain name')

