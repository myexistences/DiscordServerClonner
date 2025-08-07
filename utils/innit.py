import requests
import threading
import asyncio
import base64
from pystyle import *
import random
from datetime import datetime
import os
import time
import hashlib
import sys

# Attribution protection - checks multiple indicators
def verify_attribution():
    """Verify that proper attribution is maintained"""
    current_file = __file__
    
    # Check if the attribution is present in the logo function
    try:
        with open(current_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        required_elements = [
            "@myexistences",
            "github.com/myexistences",
            "MADE BY"
        ]
        
        missing_elements = []
        for element in required_elements:
            if element.lower() not in content.lower():
                missing_elements.append(element)
        
        if missing_elements:
            print(f"{Colors.red}⚠️  Attribution Notice ⚠️{Colors.white}")
            print(f"{Colors.yellow}Missing required attribution elements: {', '.join(missing_elements)}{Colors.white}")
            print(f"{Colors.cyan}Please maintain proper attribution to @myexistences{Colors.white}")
            print(f"{Colors.cyan}GitHub: https://github.com/myexistences{Colors.white}")
            print("\nThis tool was created with effort and should be credited appropriately.")
            print("Continuing in 5 seconds...")
            time.sleep(5)
            
    except Exception as e:
        print(f"{Colors.yellow}Could not verify attribution: {e}{Colors.white}")

def logo():
    # Verify attribution before showing logo
    verify_attribution()
    
    l = """
 __  __           ______          _         _                                      
|  \/  |         |  ____|        (_)       | |                                     
| \  / |  _   _  | |__    __  __  _   ___  | |_    ___   _ __     ___    ___   ___ 
| |\/| | | | | | |  __|   \ \/ / | | / __| | __|  / _ \ | '_ \   / __|  / _ \ / __|
| |  | | | |_| | | |____   >  <  | | \__ \ | |_  |  __/ | | | | | (__  |  __/ \__ \\  
|_|  |_|  \__, | |______| /_/\_\ |_| |___/  \__|  \___| |_| |_|  \___|  \___| |___/   

                              MADE BY @myexistences
                      Github : https://github.com/myexistences
           """
    c = Colorate.Horizontal(Colors.blue_to_purple, l)
    print(c)
    
    # Additional attribution reminder
    print(f"{Colors.dark_blue}{'='*80}{Colors.white}")
    print(f"{Colors.cyan}🔹 Original Author: @myexistences{Colors.white}")
    print(f"{Colors.cyan}🔹 If you found this useful, please give credit!{Colors.white}")
    print(f"{Colors.dark_blue}{'='*80}{Colors.white}\n")

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def current_time():
    return datetime.now().strftime("%H:%M:%S")

# Color definitions
b = Colors.dark_blue
r = Colors.red
g = Colors.green
y = Colors.yellow
w = Colors.white

# Additional protection: Add copyright notice to every major function
COPYRIGHT_NOTICE = """
# This software was created by @myexistences
# GitHub: https://github.com/myexistences
# Please maintain attribution when using or modifying this code
"""