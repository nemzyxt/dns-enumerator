# Author : Nemuel Wainaina
# Program to fetch DNS Records for a target domain and display them to the user

import sys
import dns.resolver as dns
from colorama import init, Fore

init()
GREEN = Fore.GREEN
CYAN = Fore.CYAN
GRAY = Fore.LIGHTBLACK_EX
RED = Fore.RED
RESET = Fore.RESET

RECORD_TYPES = ['A', 'AAAA', 'CNAME', 'NS', 'MX', 'SOA', 'TXT']

def enum(target):
    print(f"{GREEN}[+] DNS Records for {target}\n {RESET}")
    for record in RECORD_TYPES:
        try:
            answer = dns.resolve(target, record)
            print(f"{CYAN}{record} Records :{RESET}")
            for ans in answer:
                print("\t" + ans.to_text())
        
        except dns.NoAnswer:
            pass

        except dns.NXDOMAIN:
            print(f"{GRAY}The domain {target} doesn't exist! {RESET}")
            break

        except KeyboardInterrupt:
            print(f"{GRAY}Oops! The program terminated! Bye:) {RESET}")
            break

        else:
            print("\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{RED}Syntax : python dnsenum.py <DOMAIN_NAME> {RESET}")
    
    else:
        domain = sys.argv[1]
        if domain.startswith("www."):
            enum(domain[4:])
        else:
            enum(domain)
