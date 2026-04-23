# enumerate the directory as listed in wordlist2.txt

import requests
import sys

dir_list = open("wordlist2-1626415171030.txt").read()
directories = dir_list.splitlines()

for directory in directories:
    print(directory)
    #  when executing python from command line sys.argv[0] always accepts the filename
    #  execute the sys.argv from the command line
    #  e.g. python3 filename.py website.com
    dir_enum = f"http://{sys.argv[1]}/{directory}.html"
    r = requests.get(dir_enum)
    if r.status_code == 404:
        pass  # this means this code doesn't do anything
    else:
        print(f"{directory} is a valid directory")
