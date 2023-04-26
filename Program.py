import re
import urllib
from headers import *
from vulnz import * # module to check for vulnerabilities

print(ga.green+'''
            
                                                                                                                                         
                                                    
        ****************************************************************************
        *| "WebScript" Web Applications Security Scanner                    *
        *|  This Version Supports Remote Code/Command Execution, XSS               *
        *|  And SQL Injection.                                                     *
        ****************************************************************************
        '''+ga.end)

def urls_or_list(): # user wants to scan a single URL or a list of URLs.
    url_or_list = input(" [!] Scan URL or List of URLs? [1/2]: ")
    if url_or_list == "1":
        url = input(" [!] Enter the URL: ")
        # if not url.startswith("http://"):
        #     # Thanks to Nu11 for the HTTP checker
        #     print ga.red+'''\n Invalid URL, Please Make Sure That The URL Starts With \"http://\" \n'''+ga.end
        #     exit()
        # If the URL is valid and contains a query string
        if "?" in url:
            rce_func(url)
            xss_func(url)
            error_based_sqli_func(url) 
        # If the URL is not valid, the function prints a warning message and continues to the next URL in the list.
        else:
            print(ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end)            
            print(ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end)
            exit()
    elif url_or_list =="2":
        urls_list = input(ga.green+" [!] Enter the list file name .e.g [list.txt]: "+ga.end)
        open_list = open(urls_list).readlines()
        for line in open_list:
            if "?" in line:
                links = line.strip()
                url = links
                print(ga.green+" \n [!] Now Scanning %s"%url +ga.end)
                rce_func(url)
                xss_func(url)
                error_based_sqli_func(url)
            else:
                links = line.strip()
                url = links
                print(ga.red +"\n [Warning] "+ ga.end + ga.bold+"%s"%url +ga.end + ga.red +" is not a valid URL"+ga.end)                
                print(ga.red +" [Warning] You should write a Full URL .e.g http://site.com/page.php?id=value \n"+ ga.end)
        exit()                

urls_or_list()
