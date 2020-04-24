#!/usr/bin/python3
import time
from colorama import Fore
from colorama import init
init(autoreset = True)
from subprocess import call , PIPE



class Config_Tor(object):
    def __init__(self):
        self.torrc = "/etc/tor/torrc"
        self.report_t = r'''
Already configured . If the Tor service doesn't work for you , 
Please Configure Manually Or Report Support Via Github , Telegram , Youtube, !!!
Github : https://github.com/reza-tanha/
Telegram : https://T.me/S3CURITY_GARY
Youtube : https://bit.ly/2yas3rm'''
        self.text_1 = r''' 
UseBridges 1
ClientTransportPlugin obfs3 exec /usr/bin/obfsproxy managed
ClientTransportPlugin obfs4 exec /usr/bin/obfs4proxy managed
        '''
        self.text_2 = r'''
        
Bridge obfs4 161.97.248.185:9030 E795F5705ADF1EC8A9A525E2AA82CABF025457A0 cert=Y5WYkpNJ+tHaeMawMfmYUWAZekysqHXX856uW5q6BWrJQVEydVzVFkID/2bUgVeGLYmvLg iat-mode=0
Bridge obfs4 125.212.251.104:6666 60B0409FF87E05CD1C88A7FB01E221E54A05EEA4 cert=K8j50CA2dN9mNF0sHB5nfI/AUMUxJumJejv7gl9IaIsJ2vS0icfexHJygze9/sXlimTAJQ iat-mode=0
Bridge obfs4 95.216.186.68:1192 CD6A3B2F22509345DB47F64B2A26FB6A601A1FA0 cert=1gRAX5LV2NQGphZgGTwQumnh01/LwThkRbUmiX7wwAJARWxx2hjBAT3dhbpy/QoyqRmZHg iat-mode=0


        '''

        self.banner_t = r"""     
        
                    +++++++++++++++++++++++++++++++++++++++++++++++++++++
                    #    Tor Bridge Script                              #
                    #    Version 1.0                                    #
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
            print(Fore.LIGHTCYAN_EX+x, end='', flush=True)
            time.sleep(0.002)
        print()



    def install_de(self):
        try:
            call(["sudo", "apt-get", "install", "obfs4proxy", "obfsproxy", "-y"], stdout=PIPE)
        except:
            print(Fore.RED + "Please manually install obfs4proxy, obfsproxy, tor")
            print(Fore.CYAN+"sudo apt-get install obfs4proxy obfsproxy tor")

        try:
            with open(self.torrc, "r") as check:
                if (self.text_1.strip() and self.text_2.strip()) in check.read():
                    for x in self.report_t:
                        print(Fore.LIGHTMAGENTA_EX + x, end='', flush=True)
                        time.sleep(0.003)
                    print()
                else:
                    with open(self.torrc, "a+") as test:
                        test.write(self.text_1+"\n"+self.text_2)
                    call(["service" , "tor", "restart"])
                    print(Fore.LIGHTGREEN_EX + "Successfully configured :) ")


        except KeyboardInterrupt:
            print("canceled")


if __name__ == '__main__':
    T = Config_Tor()
    T.banner()
    T.install_de()

