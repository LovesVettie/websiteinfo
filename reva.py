import colorama
from colorama import Fore, Back, Style
import time
import os
import requests
import socket
import random

banner = """

██████╗ ███████╗██╗   ██╗ █████╗     ██╗    ██╗███████╗██████╗     ██╗███╗   ██╗███████╗ ██████╗ 
██╔══██╗██╔════╝██║   ██║██╔══██╗    ██║    ██║██╔════╝██╔══██╗    ██║████╗  ██║██╔════╝██╔═══██╗
██████╔╝█████╗  ██║   ██║███████║    ██║ █╗ ██║█████╗  ██████╔╝    ██║██╔██╗ ██║█████╗  ██║   ██║
██╔══██╗██╔══╝  ╚██╗ ██╔╝██╔══██║    ██║███╗██║██╔══╝  ██╔══██╗    ██║██║╚██╗██║██╔══╝  ██║   ██║
██║  ██║███████╗ ╚████╔╝ ██║  ██║    ╚███╔███╔╝███████╗██████╔╝    ██║██║ ╚████║██║     ╚██████╔╝
╚═╝  ╚═╝╚══════╝  ╚═══╝  ╚═╝  ╚═╝     ╚══╝╚══╝ ╚══════╝╚═════╝     ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
                                                                                                 
[+]By H04x


"""
hizmetler = """
1 | Çıkış
2 | Terminali Temizle
3 | Robots.TXT
4 | IP ADRESI
5 | Port Tarama

"""
print(Fore.RED)
print(banner)

print(Fore.GREEN)
sitegir = input("Lütfen Bir Websitesi Gir root$kali: ")
time.sleep(2)
print("Başarıyla Site Girildi: ",sitegir)
time.sleep(2)

print(Fore.BLUE)
print(hizmetler)


def main():
    while True:
        soru1 = input("Hizmet Girin root$kali: ")
        if soru1 == "1":
            exit()

        elif soru1 == "2":
            os.system(cls)

        elif soru1 == "3":
            print(Fore.GREEN)
            print(sitegir,"/robots.txt")
            print(Fore.RED)

        elif soru1 == "4":
            print(Fore.RED)
            website = sitegir
            ip_add = socket.gethostbyname(website)
            print(Fore.GREEN)
            print("IP Adresi Bulundu root$kali:", ip_add)
            print(Fore.RED)

        elif soru1 == "5":
            print(Fore.RED)
            Server = input("Taramak İstenilen IP Adresini Gir root$kali: ")
            baslangic = int(input("Başlangıç Portu Gir root$kali: "))
            bitis = int(input("Bitiş Portu Gir root$kali: "))
            ServerIp = socket.gethostbyname(Server)

            for port in range(baslangic,bitis):
                sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                result = sock.connect_ex((ServerIp,port))
                if result == 0:
                    print("Port {}: Açık Port".format(port))
                else:
                    print("Port {}: Kapalı Ports".format(port))
                sock.close()








        else:
            print("Lütfen Geçerli Bir Hizmet Girin")


if __name__ == "__main__":
    main()
