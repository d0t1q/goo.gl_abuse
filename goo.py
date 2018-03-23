import itertools
import string

chars = string.ascii_letters + string.digits
for url in itertools.permutations(chars, 6):
        full_url = "http://goo.gl/" + "".join(url)
        try:
            request_url = urllib2.urlopen(full_url).geturl()
            with open('urls.txt', 'a') as f:
                f.write("Requested Short URL: "+full_url+" Unshortened version: "+request_url+'\n')
                f.close()
                sleep(0.5)
            except Exception as e:
                sleep(1)
