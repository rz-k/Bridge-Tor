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
Bridge 193.77.153.221:9001 1948FEF52897F6A25E456B7DB9C2D37EFB7250C1
Bridge 50.3.72.238:20338 EF870A94B09A90C3C5E3BD6115C33635CDE5D100
Bridge 173.61.137.53:9991 A7414D48F264354CB4E92A9551D661AA5605E3D9
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

