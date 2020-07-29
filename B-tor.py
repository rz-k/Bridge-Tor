#!/usr/bin/python3
import time
import platform
import os
from colorama import Fore
from colorama import init

init(autoreset=True)
from subprocess import call, PIPE, check_call


class Config_Tor(object):
    def __init__(self):
        self.torrc = "/etc/tor/torrc"
        self.report_t = r'''
Already configured . If the Tor service doesn't work for you , 
Please Configure Manually Or Report Support Via Ip_info , Telegram , Youtube, !!!
Ip_info : https://github.com/reza-tanha/
Telegram : https://T.me/S3CURITY_GARY
Youtube : https://bit.ly/2yas3rm'''
        self.text_1 = r''' 
UseBridges 1
ClientTransportPlugin obfs3 exec /usr/bin/obfsproxy managed
ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy managed
'''
        self.text_2 = r'''

Bridge obfs4 121.7.172.42:12988 F622A244CCD32CD2C69C03A27820B0A66E473AB1 cert=boJhEy16J4WUW8BzZR/2YBG1rEhc0gqwsjMyTsbvhmLmh2ZGMEth9d7ToBcl1a7y1MZfAw iat-mode=0
Bridge obfs4 185.220.101.190:41249 1750BCB4E71C958660741F0196A17D7B311C83B4 cert=p9L6+25s8bnfkye1ZxFeAE4mAGY7DH4Gaj7dxngIIzP9BtqrHHwZXdjMK0RVIQ34C7aqZw iat-mode=0
'''

        self.banner_t = r"""     

                    +++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #    Tor Bridge Script                              #
                    #    Version 1.2.0                                  #
                    #    Github : https://github.com/reza-tanha/        #
                    #    Telegram : T.me/S3CURITY_GARY                  #
                    #    Youtube : https://bit.ly/2yas3rm               #
                    #    Code By : Haji (Reza)                          #
                    #                                                   #
                    #    Gray Security Team                             #
                    +++++++++++++++++++++++++++++++++++++++++++++++++++++

            """

    def banner(self):
        for x in self.banner_t:
            print(Fore.LIGHTCYAN_EX + x, end='', flush=True)
            time.sleep(0.002)
        print()

    #=====================================

    def is_obfsproxy(self):
        x = call("ls /usr/bin/ | grep obfsproxy", shell=True, stdin=PIPE)
        if x == 0:
            return True
            # print("y")
        else:
            # print("n")
            return False

    def is_obfs4proxy(self):
        x = call("ls /usr/bin/ | grep obfs4proxy", shell=True, stdin=PIPE)
        if x == 0:
            return True
        else:
            return False

    def getMachine(self):
        x = platform.machine()
        if x.strip() == 'x86_64':
            return '64'
        else:
            return '32'

    def ins_obfsproxy(self):
        try:
            call(["sudo", "dpkg", "-i", "obfs/obfsproxy_all.deb"], stdout=PIPE)
        except:
            pass

    def ins_obf4sproxy_64(self):
        try:
            # call(["sudo", "dpkg", "-i", "obfs/obfs4proxy_amd64.deb"], stdout=PIPE)
            call(["sudo", "apt", "install", "./obfs/obfs4proxy_amd64.deb","-y"], stdout=PIPE)
        except:
            pass

    def ins_obf4sproxy_32(self):
        try:
            # call(["sudo", "dpkg", "-i", "obfs/obfsproxy_all.deb"], stdout=PIPE)
            call(["sudo","apt", "install", "./obfs/obfsproxy_all.deb", "y"], stdout=PIPE)

        except:
            pass

    #=====================================

    def install_obfs4proxy(self):
        try:
            # call(["sudo", "apt-get", "install", "obfs4proxyxxxx", "-y"], stdout=PIPE)
            if self.is_obfs4proxy() != True:
                if self.getMachine() == '64':
                    self.ins_obf4sproxy_64()
                    print(Fore.LIGHTGREEN_EX + "[✅] Install obfs4proxy [✅]")
                else:
                    self.ins_obf4sproxy_32()
                    print(Fore.LIGHTGREEN_EX + "[✅] Install obfs4proxy [✅]")
            else:
                print(Fore.LIGHTGREEN_EX + "[✅] obfs4proxy exists [✅]")
        except:
            pass
    def install_obfsproxy(self):
        try:
            # call(["sudo", "apt-get", "install", "obfsproxyxxxx", "-y"], stdout=PIPE)
            if self.is_obfsproxy() != True:
                self.ins_obfsproxy()
                print(Fore.LIGHTGREEN_EX + "[✅] Install obfsproxy [✅]")
            else:
                print(Fore.LIGHTGREEN_EX + "[✅] obfsproxy exists [✅]")

        except:
            self.ins_obfsproxy()


    def check_to_text(self):
        check = open(self.torrc, "r").read()
        if (self.text_1.strip() in check) and (self.text_2.strip() in check):
            return True
        else:
            return False


    def check_text_one(self):
        check = open(self.torrc, "r").read()
        if self.text_1.strip() in check:
            pass
        else:
            check1 = open(self.torrc, "a")
            check1.write(self.text_1.strip() + "\n")

    def check_text_tow(self):
        check2 = open(self.torrc, "r").read()
        if self.text_2.strip() in check2:
            pass
        else:
            check2 = open(self.torrc, "a")
            check2.write(self.text_2.strip() + "\n")

    def text_exiest(self):
        for x in self.report_t:
            print(Fore.LIGHTMAGENTA_EX + x, end='', flush=True)
            time.sleep(0.003)
        print()

if __name__ == '__main__':

    T = Config_Tor()
    T.banner()
    # if T.is_obfs4proxy() != True:
    T.install_obfs4proxy()
    # if T.is_obfsproxy() != True:
    T.install_obfsproxy()

    if T.check_to_text():
        T.text_exiest()
    else:
        T.check_text_one()
        T.check_text_tow()
        call(["service", "tor", "restart"])
        print(Fore.LIGHTGREEN_EX + "[✅] Successfully configured [✅] ")


