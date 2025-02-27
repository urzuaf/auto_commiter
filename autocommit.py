import os
import random
import time

REPO_PATH = "."  # path to repo
os.chdir(REPO_PATH)
last_number=0

filename = "auto_commit_log"

def getLastNumber():
    global last_number
    if os.path.exists(filename):
        with open(filename, "r") as f:
            lines = f.readlines()
    
        if lines:
            last_number = int(lines[-1].strip()) 

def writeLastNumber():

    # write next number
    with open(filename, "a") as f:
        f.write(f"{last_number + 1}\n")

def push():
    randnumber = random.randint(5,10)
    cont = 0
    for (cont < randnumber):
        cont = cont + 1
        # Git commands
        os.system("git add .")
        os.system(f'git commit -m "Commit automático {last_number + 1}"')
        os.system("git push origin main")
        time.sleep(5)
