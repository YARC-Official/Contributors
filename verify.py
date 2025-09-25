import json
import os
import sys

hasError = False
seen_names = [ ]
def CI(message, isError=False):
    global hasError
    if isError:
        hasError = True
    if os.getenv("CI"):
        print(message)

def check_names():
    with open("contributors.json") as f:
        contributors = json.load(f)
        
        # Check for duplicate name entries
        for contributor in contributors:
            if contributor["Name"] in seen_names:
                print(f"Duplicate name entry: {contributor['Name']}")
                CI(f"Duplicate name entry found: {contributor['Name']}", isError=True)
                continue
                
            seen_names.append(contributor["Name"])

if __name__ == "__main__":
    check_names()
    if hasError:
        sys.exit(1)
