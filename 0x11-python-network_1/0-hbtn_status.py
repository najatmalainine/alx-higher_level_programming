#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
The body of the response must be displayed like the following example (tabulation before -)"""

import urllib.request

if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        html = response.read()
        print("Body response:")
        print("\t- type:", type(html))
        print("\t- content:", html)
        print("\t- utf8 content: {}".format(html.decode('utf-8')))
