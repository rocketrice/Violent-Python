import zipfile
import optparse
from threading import Thread
import time


def extractFile(zFile, password):
    try:
        zFile.extractall(pwd=password)
        print "\n[+] Password found: " + password + "\n"
        exit(0)
    except Exception, e:
        pass
        
def main():
    parser = optparse.OptionParser("usage%prog " + "-f <zipfile> -d <dictionary>")
    parser.add_option('-f', dest='zname', type='string', help="Specify ZIP file.")
    parser.add_option('-d', dest='dname', type='string', help='Specify dictionary file.')
    (options, args) = parser.parse_args()
    
    if (options.zname == None) | (options.dname == None):
        print parser.usage
        exit(0)
    else:
        zname = options.zname
        dname = options.dname
    
    try:
        zFile = zipfile.ZipFile(zname)
    except:
        print "[-] ZIP file not found \n"
        exit(0)
    
    try:
        passFile = open(dname)
    except:
        print "[-] Dictionary not found \n"
        exit(0)
    
    print "\n[*] Beginning Crack on " + zname + " with " + dname + "\n"
    
    
    for line in passFile.readlines():
        password = line.strip("\n")
        t = Thread(target=extractFile, args=(zFile, password))
        t.start()
    
    time.sleep(10)
    
    print "\n[-] If no response is visable, the attack failed.\n"
    exit(0)
            
if __name__ == "__main__":
    main()