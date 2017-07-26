import optparse
from socket import *
from threading import *

screenLock = Semaphore(value = 1)

def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('Aloha Snack Bar\r\n')
        results = connSkt.recv(1024)
        screenLock.acquire()
        print '[+]%d/tcp open'% tgtPort
        print '[+] ' + str(results) + '\n'
    except:
        screenLock.acquire()
        print '[-]%d/tcp closed\n'% tgtPort
    finally:
        screenLock.release()
        connSkt.close()
        
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print "[-] Cannot reslove '%s%': Unknown host"% tgtHost
        return
    try:
        tgtName = gethostbyaddr
        print '\n[+] Scan Results for: ' + tgtName[0] + '\n'
    except:
        print '\n[+] Scan Results for: ' + tgtIP + '\n'
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
        t = Thread(target=connScan, args=(tgtHost, int(tgtPort)))
        t.start()
        
def main():
    parser = optparse.OptionParser('usage %prog -H <target host> -p <target port[s]>')
    parser.add_option('-H', dest='tgtHost', type='string', help='specify target host')
    parser.add_option('-p', dest='tgtPorts', type='string', help='specify target port[s]')
    (options, args) = parser.parse_args()
    
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPorts).split(',')
    
    if (tgtHost == None) | (tgtPorts == None):
        print parser.usage
        exit(0)
    
    portScan(tgtHost, tgtPorts)
    
    
if __name__ == "__main__":
    main()