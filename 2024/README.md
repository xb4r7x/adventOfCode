# adventOfCode2024
![](https://img.shields.io/badge/day%20📅-3-blue)
![](https://img.shields.io/badge/stars%20⭐-4-yellow)	
![](https://img.shields.io/badge/days%20completed-2-red)

https://adventofcode.com/2024

# newDay.sh
This script will create the directory structure, create a basic python skeleton, and activate our Pyton virtual environment (precreated).
It takes the day as an argument. If no argument is provided it will assume you want today.
The python skeleton generated requires that your adventofcode.com session cookie be stored in an environment variable $AOC_SESSION and it also requires the aocd libray is installed. (https://pypi.org/project/advent-of-code-data/#description)

#### Obtaining session cookie
- Log into adventofcode.com
- Navigate to any day's input page
- Open your browser's dev tools and find your session cookie in the request headers or under cookies in the Application tab.
- The same session cookie should be valid for the whole month, so you should only have to do this once. 
- Export this cookie in the $AOC_SESSION env var. Consider placing it in your shell profile so any terminals you open will have it ready.

# Python venv
This year I'll be using a venv for handling dependencies and whatnot. To create the venv:
- `virtualenv --python=python3 venv`
- `source ./venv/bin/activate`

# pip Installed packages
- `pip install advent-of-code-data`

# Folder Structure
Each day of the advent calendar has its own numbered folder. All files to solve the problems of the day will be placed inside that folder. 
