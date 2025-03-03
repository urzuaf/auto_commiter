import os
import random
import time

REPO_PATH = "."  # path to repo
os.chdir(REPO_PATH)
last_number=0

filename = "auto_commit_log"

def getLastNumber():
    global last_number
    last_number = 0
    if os.path.exists(filename):
        with open(filename, "r") as f:
            lines = f.readlines()
    
        if lines:
            last_number = int(lines[-1].strip()) 
    return last_number

def writeLastNumber():
    # write next number
    with open(filename, "a") as f:
        f.write(f"{last_number + 1}\n")

randnumber = random.randint(12,25)
print(f"Number of commits: {randnumber}")
cont = 0
while cont < randnumber:
    last_number = getLastNumber()
    writeLastNumber()
    os.system("git add .")
    os.system(f'git commit -m "auto commit {last_number + 1}"')
    print(f"Pushed commit {cont + 1}")
    cont = cont + 1

os.system("git push origin main")
