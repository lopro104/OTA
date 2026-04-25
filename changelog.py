import datetime
import requests

android = "16"
currentQPR = 2
day = datetime.datetime.now().day
month = datetime.datetime.now().strftime("%B")
year = datetime.datetime.now().year
month2 = datetime.datetime.now().month

print("date is", day,month,year)

something = f"{day}/{month2}/{year}"

nrchanges = requests.get("https://raw.githubusercontent.com/Evolution-X/changelog/bka/changelogs/LATEST.txt")

if nrchanges.ok:
   changes = nrchanges.text
else:
    changes = "* Could not fetch ROM changes at this time."

numberofchanges = int(input("How many changes?:"))

allchanges = []

for i in range(numberofchanges):
    entry = input(f"Change #{i+1}: ")
    allchanges.append(f"* {entry}")
    
finalchanges = "\n\n".join(allchanges)

changelog = f"""This is Android {android} QPR{currentQPR} with {month} {year} security patches

Notes:
==============================
- LineageOS-based source. Signed build.
- Make sure to be on Pixel 4a firmware first.
- Clean flash is required if coming from March 2024 or older builds.
- Always dirty flash at your own risk. If your device bootloops, revert to an older build that boots.
- Magisk is supported.
- Play Integrity passes, RCS works (As of {something}).
- Includes LineageOS camera.

Device changes:
==============================
{finalchanges}

{changes}
"""

with open("Changelog.txt", "w") as newchangelog:
     newchangelog.write(changelog)

