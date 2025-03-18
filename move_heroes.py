#!/usr/bin/env python3
"""Move and Rename Files with shutil"""

import shutil  # For moving and renaming files
import os  # For directory operations

def main():
    """Main logic"""
    # Ensure the script starts in the correct directory
    os.chdir("/home/student/mycode/")

    if os.path.exists("/home/student/mycode/battlecruiser/"):
        # Move Raynor to battlecruiser
        print('Directory: /home/student/mycode/battlecruiser/, exist')
        shutil.move("raynor.obj", "battlecruiser/")
    else:
        print('Directory: /home/student/mycode/battlecruiser/, does not exist')

    # Prompt for Kerrigan's new name
    xname = input("What is the new name for kerrigan.obj? ")

    # Rename Kerrigan
    if os.path.exists("/home/student/mycode/battlecruiser/lola.obj"):
        print('File: /home/student/mycode/battlecruiser/lola.obj, already exist')
        exit()
    else:
       shutil.move("battlecruiser/kerrigan.obj", f"battlecruiser/{xname}")

main()

