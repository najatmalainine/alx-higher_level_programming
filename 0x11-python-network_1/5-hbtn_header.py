#!/usr/bin/python3
"""
a Python script that fetches https://alx-intranet.hbtn.io/status
using the package requests
"""

import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    print(r.headers.get('X-Request-Id'))
