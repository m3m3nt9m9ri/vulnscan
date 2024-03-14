import os
import time
import requests
import subprocess
from colorama import init, Fore, Back, Style

banner = """


                                                                                                          
██╗   ██╗██╗   ██╗██╗     ███╗   ██╗███████╗ ██████╗ █████╗ ███╗   ██╗
██║   ██║██║   ██║██║     ████╗  ██║██╔════╝██╔════╝██╔══██╗████╗  ██║
██║   ██║██║   ██║██║     ██╔██╗ ██║███████╗██║     ███████║██╔██╗ ██║
╚██╗ ██╔╝██║   ██║██║     ██║╚██╗██║╚════██║██║     ██╔══██║██║╚██╗██║
 ╚████╔╝ ╚██████╔╝███████╗██║ ╚████║███████║╚██████╗██║  ██║██║ ╚████║
  ╚═══╝   ╚═════╝ ╚══════╝╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
     
               ###################################
               #     CyberDark VulnScan Tool     #
               #        Developer by R1o         #        
               #                                 #
               ###################################                                                                                                                         
                          Version:0.1
"""

print(Style.BRIGHT + Fore.RED + banner)


if os.geteuid() != 0:
    print("You must have root privileges to use this tool!")
    print("Please run it again using the 'sudo' command.")
    exit(1)

#Hedef site alaq
selection = input(Style.BRIGHT + Fore.YELLOW + "Target Site: ")
os.system("clear")
#Saytin islek olub olmadigini yoxlamaq ucun sorgu gonderek
try:
       
    test = requests.get("https://" + selection)

    if test.status_code ==200:
        print(Style.BRIGHT + Fore.BLUE + "[+]" , Fore.GREEN + " A connection to the site has been established and the scan begins ... " )
        time.sleep(5)  
        print(Style.BRIGHT + Fore.BLUE + "[+]" , Fore.GREEN + " Retrieving Whois Information ...")
        time.sleep(5)
        print(Style.BRIGHT + Fore.RED + """
                                                
               \    / |_   _  o  _ 
                \/\/  | | (_) | _> 
                                    

    """)
        print(Style.BRIGHT + Fore.BLUE + "[+]" + Fore.GREEN + " Whois scan Started ...")
        time.sleep(5)
        os.system("dmitry " + selection )
        
        time.sleep(5) 
        print(Style.BRIGHT + Fore.BLUE + "[+]" , Fore.GREEN + " Whois scan finished ...\n\n\n")
        print(Style.BRIGHT + Fore.RED + """

                                    __            
                |\ | o | _|_  _    (_   _  _. ._  
                | \| | |< |_ (_)   __) (_ (_| | | 
                                                
    """)
        print(Style.BRIGHT + Fore.BLUE + "[+]" + Fore.GREEN + " Nikto scan Started ...")
        time.sleep(5)
        os.system("nikto -h https://" + selection)
        print(Style.BRIGHT + Fore.BLUE + "[+]" , Style.BRIGHT + Fore.GREEN + " Nikto scan is finished ...\n\n\n")
        time.sleep(5)

        print(Style.BRIGHT + Fore.RED + """



                        
                                    ___  _            _                  ___               
                    |   \(_)_ _ ___ __| |_ ___ _ _ _  _  / __| __ __ _ _ _  
                    | |) | | '_/ -_) _|  _/ _ \ '_| || | \__ \/ _/ _` | ' \ 
                    |___/|_|_| \___\__|\__\___/_|  \_, | |___/\__\__,_|_||_|
                                                    |__/                     

    """)
        print(Style.BRIGHT + Fore.GREEN + "[+]" , "Secret Directory search begins ...")
        time.sleep(3)
        os.system("sudo dirsearch -h" + "https://" + selection)
        time.sleep(5)
        print("\n\n\n")
        print(Style.BRIGHT + Fore.BLUE + "[+]" , Style.BRIGHT + Fore.GREEN + " Directory Scan is finished ...\n\n\n")
    else:
        print(Style.BRIGHT + Fore.GREEN + "[+]" , "The website is wrong ...")
except requests.exceptions.RequestException as e:
    print("Eror:", e)

