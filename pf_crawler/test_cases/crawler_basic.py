import re, urllib, md5


def crawl_a():
    """
    found and copied a basic spider 
    @http://null-byte.wonderhowto.com/inspiration/basic-website-crawler-python-12-lines-code-0132785/
    """
    textfile = file('depth_1.txt','wt')
    print "Enter the URL you wish to crawl.."
    print 'Usage  - "http://intranic.net/" <-- With the double quotes'
    myurl = input("@> ")
    for i in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I):
        print i 
        for ee in re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(i).read(), re.I):
            print ee
            textfile.write(ee+'\n')
    
    textfile.close()


#contrived functions to imitate the above function with a bit more flexibility and recursiveness
def fetch_all_href(content):
    return re.findall('''href=["'](.[^"']+)["']''', urllib.urlopen(myurl).read(), re.I): or []

def crawl_b(dest, parent):
    this_hash = 'somehash' #build with md5
    for _url in fetch_all_href(dest):
        #log as (_url, parent)
        crawl_b(_url, this_hash)
    
