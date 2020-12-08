#!/usr/bin/env python3
# a cannabis dose calculator. this is a simple attempt
# to sort the logic out prior to adding Flask

import sys

# print("what?")
if len(sys.argv) == 1:
    print("\n\nSimple THC edible dose calculator for WNN\n")
    print("USE: SimpleDoseCalc.py <grams of cannabis> <TAC %> <cups of oil/butter> <total servings>\n")
    sys.exit()
elif len(sys.argv) == 5:
    cannabis = sys.argv[1]
    tac = sys.argv[2]
    fat = sys.argv[3]
    servings = sys.argv[4]
else:
    print("\nsomething went really wrong\n")
    print("USE: SimpleDoseCalc.py <grams of cannabis> <TAC %> <cups of oil/butter> <total servings>\n")
    sys.exit()

cannabis_mg = int(cannabis) * 10
cannabis_mg_thca = int(cannabis_mg) * 0.877
total_mg = int(cannabis_mg) // int(cannabis_mg)
infusion_mg = int(fat) // int(servings)

print("sweet\n")
sys.exit()