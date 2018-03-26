#!/usr/bin/python
import urllib2
import itertools
import string
from time import sleep

chars = string.ascii_letters + string.digits
for url in itertools.permutations(chars, 6):
        full_url = "http://goo.gl/" + "".join(url)
        try:
            request_url = urllib2.urlopen(full_url).geturl()
            with open('goo.gl_urls.csv', 'a') as f:
                f.write(full_url+","+request_url+'\n')
                f.close()
                sleep(0.5)
        except Exception as e:
            e = str(e)
            if "404" not in e:
                with open('urls.txt', 'a') as f:
                    f.write(full_url+","+e+'\n')
                    f.close()
            else:
                pass
            sleep(1)
            
