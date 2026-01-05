import os
import time
from pystyle import Center, Colorate, Colors, Banner, Write
from colorama import Style, Fore
os.system('cls')

banner2 = """
        66666666          
       6::::::6        
      6::::::6         
     6::::::6        
    6::::::6         
   6::::::6         
  6::::::6         
 6::::::::66666   
6::::::::::::::66    
6::::::66666:::::6   
6:::::6     6:::::6                 
6:::::6     6:::::6                 
6::::::66666::::::6      
 66:::::::::::::66       
   66:::::::::66      
     666666666 
                                                        """
banner3 = """
        66666666         444444444   
       6::::::6         4::::::::4  
      6::::::6         4:::::::::4  
     6::::::6         4::::44::::4      
    6::::::6         4::::4 4::::4             
   6::::::6         4::::4  4::::4              
  6::::::6         4::::4   4::::4           
 6::::::::66666   4::::444444::::444       
6::::::::::::::66 4::::::::::::::::4     
6::::::66666:::::64444444444:::::444         
6:::::6     6:::::6         4::::4               
6:::::6     6:::::6         4::::4               
6::::::66666::::::6         4::::4  
 66:::::::::::::66        44::::::44
   66:::::::::66          4::::::::4
     666666666            4444444444
                                                        """
banner4 = """
        66666666         444444444   222222222222222    
       6::::::6         4::::::::4  2:::::::::::::::22  
      6::::::6         4:::::::::4  2::::::222222:::::2 
     6::::::6         4::::44::::4  2222222     2:::::2 
    6::::::6         4::::4 4::::4              2:::::2 
   6::::::6         4::::4  4::::4              2:::::2 
  6::::::6         4::::4   4::::4           2222::::2  
 6::::::::66666   4::::444444::::444    22222::::::22   
6::::::::::::::66 4::::::::::::::::4  22::::::::222     
6::::::66666:::::64444444444:::::444 2:::::22222        
6:::::6     6:::::6         4::::4  2:::::2             
6:::::6     6:::::6         4::::4  2:::::2             
6::::::66666::::::6         4::::4  2:::::2       222222
 66:::::::::::::66        44::::::442::::::2222222:::::2
   66:::::::::66          4::::::::42::::::::::::::::::2
     666666666            444444444422222222222222222222
                                                        """
reaper = """⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣶⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⡾⠿⢿⡀⠀⠀⠀⠀⣠⣶⣿⣷⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣦⣴⣿⡋⠀⠀⠈⢳⡄⠀⢠⣾⣿⠁⠈⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⠿⠛⠉⠉⠁⠀⠀⠀⠹⡄⣿⣿⣿⠀⠀⢹⡇⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣾⡿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⣰⣏⢻⣿⣿⡆⠀⠸⣿⠀⠀⠀
⠀⠀⠀⢀⣴⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣆⠹⣿⣷⠀⢘⣿⠀⠀⠀
⠀⠀⢀⡾⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⠋⠉⠛⠂⠹⠿⣲⣿⣿⣧⠀⠀
⠀⢠⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣿⣿⣷⣾⣿⡇⢀⠀⣼⣿⣿⣿⣧⠀
⠰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⡘⢿⣿⣿⣿⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⣷⡈⠿⢿⣿⡆
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⢙⠛⣿⣿⣿⣿⡟⠀⡿⠀⠀⢀⣿⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣶⣤⣉⣛⠻⠇⢠⣿⣾⣿⡄⢻⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣦⣤⣾⣿⣿⣿⣿⣆⠁"""

cat = """
              𝓐 𝓕𝓮𝓭 𝓗𝓪𝓼 𝓢𝓮𝓮𝓴𝓮𝓭 𝓨𝓸𝓾
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⠟⠉⠀⠀⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠀⠀⠙⢻⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⣠⣄⠀⢻⣿⣿⣿⣿⣿⡿⠀⣠⣄⠀⠀⠀⢻⣿⣿⣏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣾⣿⣿⣿⣿⠀⠀⠀⠀⠰⣿⣿⠀⢸⣿⣿⣿⣿⣿⡇⠀⣿⣿⡇⠀⠀⢸⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣄⠀⠀⠀⠀⠙⠃⠀⣼⣿⣿⣿⣿⣿⣇⠀⠙⠛⠁⠀⠀⣼⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣷⣤⣄⣀⣠⣤⣾⣿⣿⣿⣿⣽⣿⣿⣦⣄⣀⣀⣤⣾⣿⣿⣿⣿⠃⠀⠀⢀⣀⠀⠀
⠰⡶⠶⠶⠶⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠉⠉⠙⠛⠋⠀
⠀⠀⢀⣀⣠⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠷⠶⠶⠶⢤⣤⣀⠀
⠀⠛⠋⠉⠁⠀⣀⣴⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣤⣀⡀⠀⠀⠀⠀⠘⠃
⠀⠀⢀⣤⡶⠟⠉⠁⠀⠀⠉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠉⠀⠀⠀⠉⠙⠳⠶⣄⡀⠀⠀
⠀⠀⠙⠁⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷"""
Creds = """
_________                    .___.__  __          
\_   ___ \_______   ____   __| _/|__|/  |_  ______
/    \  \/\_  __ \_/ __ \ / __ | |  \   __\/  ___/
\     \____|  | \/\  ___// /_/ | |  ||  |  \___ \ 
 \______  /|__|    \___  >____ | |__||__| /____  >
        \/             \/     \/               \/ """
LoginBanner = """
 _                 _       
| |               (_)      
| |     ___   __ _ _ _ __  
| |    / _ \ / _` | | '_ \ 
| |___| (_) | (_| | | | | |
\_____/\___/ \__, |_|_| |_|
              __/ |        
             |___/         """
TOSBannner = """
 (o)__(o)  .-.     oo_    
 (__  __)c(O_O)c  /  _)-< 
   (  ) ,'.---.`, \__ `.  
    )( / /|_|_|\ \   `. | 
   (  )| \_____/ |   _| | 
    )/ '. `---' .`,-'   | 
   (     `-...-' (_..--'  """

nm = os.getenv("USERNAME") or os.getenv("USER")
color = Colors
print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter(banner2)))
time.sleep(0.6)
os.system('cls')
print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter(banner3)))
time.sleep(0.6)
os.system('cls')
print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter(banner4)))
time.sleep(0.6)
os.system('cls')
clear = os.system('cls')
print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter (LoginBanner)))
print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter ('')))
Username = input(Colorate.Horizontal(color.blue_to_purple, ('Username: ')))
Password =  input(Colorate.Horizontal(color.blue_to_purple, ('Password: ')))
if Password == 'root' and Username == 'root':
     os.system('cls')
     print(Colorate.Horizontal(color.blue_to_purple, (f'W {Username}')))
     time.sleep(0.9)
     os.system('cls')
     print(Colorate.Horizontal(color.blue_to_purple, (f'We {Username}')))
     time.sleep(0.9)
     os.system('cls')
     print(Colorate.Horizontal(color.blue_to_purple, (f'Wel {Username}')))
     time.sleep(0.9)
     os.system('cls')
     print(Colorate.Horizontal(color.blue_to_purple, (f'Welo {Username}')))
     time.sleep(0.9)
     os.system('cls')
     print(Colorate.Horizontal(color.blue_to_purple, (f'Welcom {Username}')))
     time.sleep(0.9)
     os.system('cls')
     print(Colorate.Horizontal(color.blue_to_purple, (f'Welcome {Username}')))
     time.sleep(0.9)
     os.system('cls')
     
else:
     os.system('cls')
     print(Colorate.Horizontal(color.blue_to_purple, ("Wrong shit nigga")))
     time.sleep(0.9)
     os.system('cls')
     os.system(f'python "{__file__}"')
#This program is made by rtf nigger
def Space():
    print(Colorate.Horizontal(color.blue_to_purple,  Center.XCenter('')))
def HelpSpam():
        print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter("Kill yourself")))
        print(Colorate.Horizontal(color.purple_to_blue,("Kill yourself")))
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        HelpSpam()
        

def main():
    color = Colors
    os.system('title WeHateNiggers')
    os.system('cls')
    os.system('cls')
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner4)))
    print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter ("")))
    print(Colorate.Horizontal(Colors.purple_to_blue,Center.XCenter  ("╔═══════════════════════════════════════╗")))
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter ("║    [1] Wazzzzzaaaaa.py [2] IP lookup  ║")))
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter ("║    [3] Port scanner [4] Yuhh.py       ║")))
    print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter  ("║    [5] Shitty Packet sniffer          ║")))
    print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter  ("║    [6] Credits [7] Banner list        ║")))
    print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter  ("║    [8] Generate UserAgents            ║")))
    print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter  ("║    [9] Spam   [10] TOS                ║")))
    print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter  ("║    [11] 697Edr(IPLOGGER) [12] CLSTemps║")))
    print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter  ("║    [13] Clean PC [14] Pc info         ║")))
    print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter ("╚═══════════════════════════════════════╝")))
    print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter ("")))
    print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter ("")))
    choice = input(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter (f"[{nm}#root]-> ")))
    if choice == '1':
        os.system('python Wazzzzaaaa.py')
    if choice == '2':
        os.system('python IPLookup.py')
    if choice == '3':
        os.system('python PortSanner')   
    if choice == '4':
        os.system('python Yuhh.py') 
    if choice == '5':
        print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter('Shit is not working rn gang so find some random command')))
        time.sleep(0.8)
        main()
    if choice == '6':
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner2)))
        time.sleep(0.9)
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner3)))
        time.sleep(0.9)
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner4)))
        os.system('cls')
        os.system('cls')
        print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter('know who you are belive it')))
        time.sleep(1)
        os.system('cls')
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner2)))
        time.sleep(0.5)
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner2)))
        time.sleep(0.5)
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner3)))
        time.sleep(0.5)
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner3)))
        time.sleep(0.5)
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner4)))
        time.sleep(0.5)
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner4)))
        time.sleep(0.5)
        os.system('cls')
        time.sleep(1)
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner2)))
        time.sleep(0.9)
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner3)))
        time.sleep(0.9)
        os.system('cls')
        print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner4)))
        time.sleep(0.5)
        os.system('cls')
        print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter(Creds)))
        print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter("rtf cuz I made the program dumb ass")))
        input('')
        main()
    if choice == '7':
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner2)))
            time.sleep(0.9)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner3)))
            time.sleep(0.9)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner4)))
            os.system('cls')
            os.system('cls')
            print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter('know who you are belive it')))
            time.sleep(1)
            os.system('cls')
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner2)))
            time.sleep(0.5)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner2)))
            time.sleep(0.5)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner3)))
            time.sleep(0.5)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner3)))
            time.sleep(0.5)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner4)))
            time.sleep(0.5)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner4)))
            time.sleep(0.5)
            os.system('cls')
            time.sleep(1)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner2)))
            time.sleep(0.9)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner3)))
            time.sleep(0.9)
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner4)))
            time.sleep(0.5)
            os.system('cls')
            print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter(Creds)))
            os.system('cls')
            print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter(banner4)))
            os.system('cls')
            print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter(cat)))
            os.system('cls')
            print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter(reaper)))
            os.system('cls')
            os.system('cls')
            input(Colorate.Horizontal(color.blue_to_purple, Center.XCenter('Have fun nigger: ')))
            os.system('cls')
            main()
    if choice == '8':
        print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter('Do not go around leaking shit nigga')))
        time.sleep(0.7)
        os.system('cls')
        os.system('python agents.py') 
    if choice == '9':
        os.system('cls')
        print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter("Bye")))
        time.sleep(0.7)
        os.system('cls')
        print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter("Bye")))
        time.sleep(0.7)
        os.system('cls')
        print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter("Fuck")))
        time.sleep(0.7)
        os.system('cls')
        print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter("NIGGA")))
        time.sleep(0.7)
        os.system('cls')
        time.sleep(1)
        HelpSpam()
        main()
    if choice == '10':
            os.system('cls')
            print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(TOSBannner)))
            print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter("Never Skid Programs")))
            print(Colorate.Horizontal(color.blue_to_purple, Center.XCenter ("")))
            print(Colorate.Horizontal(Colors.purple_to_blue,Center.XCenter  ("")))
            print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter ("    1. No skiddding                    ")))
            print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter ("    2. Don't be a fed                  ")))
            print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter  ("    3. No CP Users                     ")))
            print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter  ("    4. No CP lovers                    ")))
            print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter  ("    5. No groomers                     ")))
            print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter  ("    6. NO SKIDS                        ")))
            print(Colorate.Horizontal(Colors.purple_to_blue, Center.XCenter ("")))
            print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter ("")))
            input(Colorate.Horizontal(color.purple_to_blue, Center.XCenter ("STOP BEING A FAGGOT")))
            main()
    if choice == '11':
            os.system('cls')
            input(Colorate.Horizontal(color.purple_to_blue, Center.XCenter("WARNING: DO NOT RUN ONLY CHANGE THE WEBHOOK")))
            os.system('python 697edr.py')
            main()
    if choice == '12':
            os.system('cls')
            input(Colorate.Horizontal(color.purple_to_blue, Center.XCenter("Are you sure you want to clear your Temps?")))
            os.system('Del %temp%')
            main()
    if choice == '13':
            input(Colorate.Horizontal(color.purple_to_blue, Center.XCenter ('Are you sure you want to clean up your Computer/PC: ')))
            os.system('cls')
            os.system("del /q /f /s %temp%\\*")
            os.system("rd /s /q C:\\$Recycle.Bin")
            os.system("ipconfig /flushdns")
            os.system("del /q /f /s C:\\Windows\\Temp\\*")
            os.system("del /q /f /s C:\\Windows\\Prefetch\\*")
            os.system('Del %temp%')
            main()
    if choice == '14':
         print(Colorate.Horizontal(color.purple_to_blue, Center.XCenter ("this a Pc info shit so yuhhhh")))
         os.system('ipconfig & systeminfo & wmic cpu get Name,NumberOfCores,NumberOfLogicalProcessors,MaxClockSpeed & wmic memorychip get Capacity,Manufacturer,PartNumber,Speed & wmic computersystem get TotalPhysicalMemory & wmic logicaldisk get Name,FileSystem,FreeSpace,Size & wmic path win32_videocontroller get Name,AdapterRAM,DriverVersion & netsh interface show interface & arp -a & netstat -ano & route print & hostname & whoami & tasklist & tasklist /svc & sc query & net user & net localgroup administrators & wmic bios get SerialNumber,Version & wmic baseboard get Manufacturer,Product,SerialNumber & net statistics workstation & (systeminfo & ipconfig /all & wmic cpu get name,NumberOfCores,NumberOfLogicalProcessors & wmic memorychip get capacity,manufacturer,partnumber,speed) > Info.txt')
         main()

if __name__ == "__main__":
    main()