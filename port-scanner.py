import socket
from sys import exit
from os import system
from colorama import Style, Fore 



class PortScanner:
    def __init__(self, ipAddr, portsNum):
        self.ipAddr = ipAddr
        self.portsNum = portsNum

        self.multiScan = []
        self.multiScanValue = False

    def checkMultiScan(self):
        if ',' in self.ipAddr:
            self.multiScanValue = True

            print(Fore.LIGHTRED_EX + "\n[*] Mulityple Scanning Selected.")
            
            for ipAddress in self.ipAddr.split(','):
                self.multiScan.append(ipAddress)

        else:
            print(Fore.LIGHTRED_EX + "\n[*] Single Scanning Selected.")


    def scanMultiTargets(self, ipsList):
        for ip in ipsList:
            print(Fore.LIGHTCYAN_EX + f'\n[!] Scanning {ip} For Open Ports :')
            
            print()
            
            for scanningPort in range(self.portsNum):
                self.scanSPort(target=ip, port=scanningPort)


    def scanSingleTarget(self):
        print(Fore.LIGHTCYAN_EX + f'\n[!] Scanning {self.ipAddr} For Open Ports :')
        
        print()

        for scanningPort in range(self.portsNum):
            self.scanSPort(target=ip, port=scanningPort)


    def scanSPort(self, target, port):
        try:
            socketObj = socket.socket()
            socketObj.connect((target, port))

            print(Fore.LIGHTGREEN_EX + f"[+] Port {port} open.")
            socketObj.close()
        except:
            pass


def main():
    system("clear")

    targetsIn = input(Fore.BLUE + "Enter Target(s) To Scan (split them by ,) >: ")
    portsIn = int(input(Fore.BLUE + "Enter Ports Number You Want To Scan (MAX=65535) >: "))

    _exec = PortScanner(targetsIn, portsIn)

    _exec.checkMultiScan()

    if _exec.multiScanValue == True:
        try: 
            _exec.scanMultiTargets(_exec.multiScan)

        except:
            print(Fore.RED + "\nAn Error Occurred: \n Check The Validation Of IP-Address.\n Or Check Your Internet Connection.")

    else:
        try: 
            _exec.scanSingleTarget(_exec.multiScan)

        except:
            print(Fore.RED + "\nAn Error Occurred: \n Check The Validation Of IP-Address.\n Or Check Your Internet Connection.")
            

if __name__ == '__main__':
    main()
    print(Style.RESET_ALL + "")
    
