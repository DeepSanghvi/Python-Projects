import time
from datetime import datetime as dt

hosts_Path = r"C:\Windows\System32\drivers\etc\hosts"
hosts_temp = "hosts"
redirect = "127.0.0.1"

websites = ["www.youtube.com", "youtube.com"]   #websites to be blocked can be modified here

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 9) < dt(dt.now().year, dt.now().month, dt.now().day, 22):
        print("Website blocked...")
        with open(hosts_Path,"r+") as file:
            content = file.read()
            for site in websites:
                if site in content:
                    pass
                else:
                    file.write(redirect+" "+site+"\n")
    else:
        print("Website unblocked...")
        with Open(hosts_Path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(site in line for site in websites):
                    file.write(line)
            file.truncate()
    time.sleep(5)
