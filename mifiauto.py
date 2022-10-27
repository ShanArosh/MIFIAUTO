
#Importing Modules
try:
    import sys
    import time
    import os.path
    from pywinauto.application import Application
    from selenium import webdriver
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.chrome.options import Options
    from modules.webdriver_auto_updater import check_driver
    from colorama import init
    from colorama import Fore
    init(autoreset=True)
except:
    print('ERROR : Dependencies are missing run requirements.py')
    input()
    sys.exit(1)
cracker_path = os.path.abspath("res/Marvell.exe")
driver_path=os.path.abspath("web-driver/chromedriver.exe")
brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"
loop2 = True
#MIFI-TOOLs [Part 1]
try:
    app = Application(backend="uia").connect(title="MIFITOOL????????       1.4.0.0")
    result='done'
except:
    app = Application(backend="uia").start(cracker_path)
    #Minimize Loop
    while loop2 is True:
        try:
            app = Application(backend="uia").connect(title="MIFITOOL????????       1.4.0.0")
            minimize=app.MIFITOOL.child_window(title="Minimize", control_type="Button").wrapper_object()
            minimize.click()
            loop2 = False
        except:
            pass
# Router Configeration
options = Options()
service =Service(driver_path)
options.binary_location = brave_path
#options.add_argument("--incognito") 
options.add_argument("--headless")
options.add_argument("user-data-dir=C:\\MIFIAUTO")
# Create new Instance of Chrome
try:
    browser =  webdriver.Chrome(service=service, options=options)
except Exception:
    print(Fore.RED + 'ERROR : Web Driver Version is Outdated')
    print(Fore.CYAN + "Connect to Internet Manually and Press Enter to Download WebDriver")
    input()
    check_driver('/web-driver')
    print(Fore.GREEN + 'Chrome Driver has Successfully Updated')
    
print("\n")
print(Fore.YELLOW + "Getting The Page..............................................................")
try:
    browser.get("http://192.168.0.1")
except:
    print("\n")
    print(Fore.RED + 'ERROR : Plug The Router Again')
    close=app.MIFITOOL.child_window(title="Close", control_type="Button").wrapper_object()
    close.click()
    input()
    sys.exit(1)
        
#browser.implicitly_wait(30)
#MIFI TOOL
print("\n")
print(Fore.YELLOW + "Unlocking With MIFIAUTO TOOL..............................................................")
#app = Application(backend="uia").connect(title="MIFITOOL????????       1.4.0.0")
unlock=app.MIFITOOL.child_window(title="???", auto_id="14", control_type="Button").wrapper_object()
unlock.click()
#app.MIFITOOL.print_control_identifiers()
try:
    ok=app.MIFITOOL.child_window(title="OK", auto_id="2", control_type="Button").wrapper_object()
    ok.click()
    close=app.MIFITOOL.child_window(title="Close", control_type="Button").wrapper_object()
    close.click()
    print("\n")
    print(Fore.RED + 'ERROR : Plug The Router Again')
    input()
    sys.exit(1)
except:None
#Type username
print("\n")
print(Fore.YELLOW + "Typing Username..............................................................")
username = browser.find_element("xpath","/html/body/div/div/div[3]/div/div[1]/input[1]")
username.send_keys("admin")
#Type Password
print("\n")
print(Fore.YELLOW + "Typing Password..............................................................")
password = browser.find_element("xpath","/html/body/div/div/div[3]/div/div[1]/input[2]")
password.send_keys("admin")
#Sign in Button
print("\n")
print(Fore.YELLOW + "Signing In to the account..............................................................") 
browser.find_element("id","btnSignIn").click()
#check msg notification
if browser.find_elements("xpath","/html/body/div[2]/span/div/div/div/span/input"):
    print("\n")
    print(Fore.YELLOW + "Closing Message Box..............................................................")
    browser.find_element("xpath","/html/body/div[2]/span/div/div/div/span/input").click()
#Internet button
print("\n")
print(Fore.YELLOW + "Connection Tab ..............................................................") 
browser.find_element("xpath","/html/body/div[3]/div[1]/div[3]/ul/li[2]/a").click()
#Checkbox
print("\n")
print(Fore.YELLOW + "Changing Settings..............................................................")
browser.find_element("xpath","/html/body/div[3]/div[2]/div[2]/form/div[13]/input").click()
#Save Config
print("\n")
print(Fore.YELLOW + "Save the Settings..............................................................") 
browser.find_element("xpath","/html/body/div[3]/div[2]/div[2]/form/div[35]/span/input").click()
try:
    close=app.MIFITOOL.child_window(title="Close", control_type="Button").wrapper_object()
    close.click()
except:None
print("\n")
print("\n")
print(Fore.YELLOW +'---------------Wait Until This Window Get Close----------------')
def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(Fore.YELLOW + timer, end="\r")
        time.sleep(1)
        t -= 1
    print(Fore.GREEN + 'Done!!')
countdown(int(10))
browser.quit()
