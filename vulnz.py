#!/usr/bin/env python
# WebScript is a Web Applications Security Scanner

import urllib
import re
import time
# Check whether headers module exists or not
try:
    from headers import *
except ImportError:
    pass

# updates:
# 1- Fixed the empty parameters issue => Done.
# 2- User agents when sending a Request => Done.
# 3- Added Error Based SQLI Detection Support => Done.
# 4- Will try to add XSS Injection in Cookies, Refere and UserAgent

def main_function(url, payloads, check):
    # This function is going to split the url and try to append payloads in every parameter value.
    with urllib.request.urlopen(url) as opener:
        vuln = 0
        if opener.code == 999:
            # Detecting the WebKnight WAF from the StatusCode.
            print(ga.red + " [~] WebKnight WAF Detected!" + ga.end)
            print(ga.red + " [~] Delaying 3 seconds between every request" + ga.end)
            time.sleep(3)
        for params in url.split("?")[1].split("&"):
            sp = params.split("=")[0]
            for payload in payloads:
                bugs = url.replace(sp, sp + str(payload).strip())
                request = urllib.request.urlopen(bugs)
                html = request.readlines()
                for line in html:
                    checker = re.findall(check, line.decode())
                    if len(checker) != 0:
                        print(ga.red + " [*] Payload Found . . ." + ga.end)
                        print(ga.red + " [*] Payload: ", payload + ga.end)
