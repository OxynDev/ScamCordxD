import random, os, time, colorama, string, threading

error = colorama.Fore.RED + " [" + colorama.Fore.RESET + "x" + colorama.Fore.RED + "] " + colorama.Fore.RESET
success = colorama.Fore.GREEN + " [" + colorama.Fore.RESET + "v" + colorama.Fore.GREEN + "] " + colorama.Fore.RESET
waiting = colorama.Fore.YELLOW + " [" + colorama.Fore.RESET + "." + colorama.Fore.YELLOW + "] " + colorama.Fore.RESET


def cls():
    os.system("cls")


class Stats():
    
    gened = 0
    solved = 0
    
def register(token):
    

    time.sleep(random.randint(0,3))
    mail = ("".join(random.SystemRandom().choice(string.ascii_lowercase + string.digits)for _ in range(12))) + random.choice(["@emtemp.com", "@fakemail.com", "@temp2.net","@zeemail.xyz"])
    print(success + "EMAIL" + mail)
    time.sleep(random.uniform(1, 7.5))
    print(waiting + "WAITING FOR CAPTCHA")
    time.sleep(random.uniform(7, 20.1))
    print(success + "CAPTCHA SOLVED")
    Stats.solved = Stats.solved + 1
    time.sleep(random.uniform(3, 7.5))
    intx = random.randint(0,10)
    if intx < 3:
        print(error + "TOKEN LOCKED")
        return
    print(success + token)
    Stats.gened = Stats.gened + 1
    time.sleep(random.uniform(1, 3))
    print(waiting + "WAITING FOR EMAIL")
    time.sleep(random.uniform(4, 7.5))
    print(success + "EMAIL SUCCESS")
    time.sleep(random.uniform(1, 3))
    


def name():
    while True:
        time.sleep(0.1)
        os.system(f"title   ZipCord GENED: {str(Stats.gened)} SOLVED: {str(Stats.solved)}")


cls()

print("""
  ______         ___              _ 
 / _  (_)_ __   / __\___  _ __ __| |
 \// /| | '_ \ / /  / _ \| '__/ _` |
  / //\ | |_) / /__| (_) | | | (_| |
 /____/_| .__/\____/\___/|_|  \__,_|
        |_|                         
       """)

print("\n")
input(" | Key: ")
time.sleep(2)
print("\n | VALID")
input("\n | Api Key: ")
input("\n | THREADS: ")
cls()
time.sleep(1)
threading.Thread(target=name).start()
for token in open("token.txt", "r").read().splitlines():
    def start():
        register(token)
    
    threading.Thread(target=start).start()
    time.sleep(1)
    