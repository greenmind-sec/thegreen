import docker


VERSION = "0.4"
import os,sys,argparse,subprocess

# Resolve URL for IP
import socket

# PDF
# TODO Create
#from reportlab.pdfgen import canvas

# Arquivo de configuração
import json

#
# Docker functions
#
def whois_ip(alvo):
    image="greenmind/whois-ip:1"
    container = client.containers.run(image, get_ip(alvo))
    saida=container.decode("utf-8")
    return saida

def sharingmyip(alvo):
    image="greenmind/sharingmyip:1"
    container = client.containers.run(image, alvo)
    saida=container.decode("utf-8")
    return saida

def whois_url(alvo):
    image="greenmind/whois-url:1"
    container = client.containers.run(image, alvo)
    saida=container.decode("utf-8")
    return saida

def crt_sh(alvo):
    image="greenmind/crt-sh:1"
    container = client.containers.run(image, alvo)
    saida=container.decode("utf-8")
    return saida

def dnslookup(alvo):
    image="greenmind/dnslookup:1"
    container = client.containers.run(image, alvo)
    saida=container.decode("utf-8")
    return saida

def google_hacking_search(alvo,escolha):
    image="greenmind/google_hacking_search:2"
    #extensoes = ["doc","docx","odt","pdf","rtf","tex","txt","wpd","3g2","3gp","avi","flv","h264","m4v","mkv","mov","mp4","mpg","mpeg","rm","swf","vob","wmv","bak","cab","cfg","cpl","cur","dll","dmp","drv","icns","ico","ini","lnk","msi","sys","tmp","ods","xls","xlsm","xlsx","c","class","cpp","cs","h","java","pl","sh","swift","vb","key","odp","pps","ppt","pptx","asp","aspx","cer","cfm","cgi","pl","css","htm","html","js","jsp","part","php","py","rss","xhtml","ai","bmp","gif","ico","jpeg","jpg","png","ps","psd","svg","tif","tiff","fnt","fon","otf","ttf","apk","bat","bin","cgi","pl","com","exe","gadget","jar","msi","py","wsf","email","eml","emlx","msg","oft","ost","pst","vcf","csv","dat","db","dbf","log","mdb","sav","sql","tar","xml","bin","dmg","iso","toast","vcd","7z","arj","deb","pkg","rar","rpm","tar.gz","z","zip","aif","cda","mid","midi","mp3","mpa","ogg","wav","wma","wpl"]

    extensoes = ["xls","pdf"]
    if escolha == "filetype":
        for e in extensoes:
            print("Analisando extensão ",e)
            print("site:" + alvo + " filetype:" + e)
            saida=subprocess.run(["docker", "run", "-it", "--rm", image, "--dork", "site:" + alvo + " filetype:" + e])
    elif escolha == "site":
        saida=subprocess.run(["docker", "run", "-it", "--rm", image, "--dork", "site:"+alvo])
    else:
        print("Erro ao usar modulos do spiderfoot")

    return saida


def shodan_search(alvo):
    image="greenmind/shodan:1"
    saida=subprocess.run(["docker", "run", "-it", "--rm", image, alvo])
    return saida

def wfuzz(alvo):
    image="greenmind/wfuzz:1"
    saida=subprocess.run(["docker", "run", "-it", "--rm",image, "--hc", "403", "-c", "-w", "/opt/bitquark_20160227_subdomains_popular_1000000.txt", "-H", "HOST: FUZZ.att.com", alvo])
    return saida

def dirsearch_module(alvo):
    image="greenmind/dirsearch:1"
    extensoes = "doc,docx,odt,pdf,rtf,tex,txt,wpd,3g2,3gp,avi,flv,h264,m4v,mkv,mov,mp4,mpg,mpeg,rm,swf,vob,wmv,bak,cab,cfg,cpl,cur,dll,dmp,drv,icns,ico,ini,lnk,msi,sys,tmp,ods,xls,xlsm,xlsx,c,class,cpp,cs,h,java,pl,sh,swift,vb ,key,odp,pps,ppt,pptx,asp,aspx,cer,cfm ,cgi,pl,css,htm,html,js,jsp,part,php,py,rss,xhtml,ai,bmp,gif,ico,jpeg,jpg,png,ps,psd,svg,tif,tiff,fnt,fon,otf,ttf,apk,bat ,bin,cgi,pl,com,exe,gadget,jar,msi,py,wsf,email,eml,emlx,msg,oft,ost,pst,vcf,csv,dat,db,dbf,log,mdb,sav,sql,tar,xml,bin,dmg,iso,toast,vcd,7z,arj,deb,pkg,rar,rpm,tar.gz,z,zip,aif,cda,mid,midi,mp3,mpa,ogg,wav,wma,wpl"
    # https://www.computerhope.com/issues/ch001789.htm
    saida=subprocess.run(["docker", "run", "-it", "--rm",image, "-u", alvo, "-e", extensoes])
    return saida

def nikto_module(alvo):
    image="greenmind/nikto:1"
    saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-h", alvo])
    return saida


# Spider Foot
def spiderfoot_modules(alvo,argumentos):
    image="greenmind/spiderfoot:1"
    if argumentos == "sfp_accounts":
        saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-m","sfp_accounts","-s", alvo, "-q"])
    elif argumentos == "sfp_dnsbrute":
        saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-m","sfp_dnsbrute","-s", alvo, "-q"])
    elif argumentos == "sfp_dnsraw":
        saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-m","sfp_dnsraw","-s", alvo, "-q"])
    elif argumentos == "sfp_dnsresolve":
        saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-m","sfp_dnsresolve","-s", alvo, "-q"])
    elif argumentos == "sfp_fringeproject":
        saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-m","sfp_fringeproject","-s", alvo, "-q"])
    elif argumentos == "sfp_spider":
        saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-m","sfp_spider","-s", alvo, "-q"])
    elif argumentos == "sfp_tldsearch":
        saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-m","sfp_tldsearch","-s", alvo, "-q"])
    elif argumentos == "sfp_urlscan":
        saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-m","sfp_urlscan","-s", alvo, "-q"])
    elif argumentos == "sfp_whois":
        saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-m","sfp_whois","-s", alvo, "-q"])
    elif argumentos == "all":
        list = ["sfp_accounts","sfp_dnsbrute","sfp_dnsbrute","sfp_dnsraw","sfp_dnsresolve","sfp_fringeproject","sfp_spider","sfp_tldsearch","sfp_urlscan","sfp_whois"]
        for module in list:
            print("Analisando modulo ",module)
            saida=subprocess.run(["docker", "run", "-it", "--rm",image,"-m",module,"-s", alvo, "-q"])
    else:
        print("Erro ao usar modulos do spiderfoot")
    return saida

def green_gethostname(url):
    name_host = socket.gethostbyname(url)
    return name_host

# Funções requisitos
def get_ip(URL):
    IP = socket.gethostbyname(URL)
    return IP

def get_url():
    IP = socket.gethostbyname(URL)
    return IP

parser = argparse.ArgumentParser(description = 'GreenMind Security Scan.')
parser.add_argument('-u', action = 'store', dest = 'url', required = True,help = 'insert target.')
parser.add_argument('-r', action = 'store', dest = 'recon', required = True,help = 'insert tool (google_hacking, whois_ip, whois_url, dnslookup, sharingmyip, crt.sh).')
parser.add_argument('-a', action = 'store', dest = 'argumentos', required = False,help = 'insert arguments')


arguments = parser.parse_args()
URL = arguments.url
RECON = arguments.recon
ARGUMENTOS = arguments.argumentos


client = docker.from_env()
# Check Google
if RECON == "google_hacking":
    print(google_hacking_search(URL,ARGUMENTOS))
# Check info whois IP
if RECON == "whois_ip":
    print(whois_ip(URL))
# Check info whois URL
if RECON == "whois_url":
    print(whois_url(URL))
# Check DNSlookup
if RECON == "dnslookup":
    print(dnslookup(URL))
# Check SharingMyIP
if RECON == "sharingmyip":
    print(sharingmyip(URL))
# Check Crt.sh
if RECON == "crt.sh":
    print(crt_sh(URL))
# Check shodan.io
if RECON == "shodan":
    print(shodan_search(URL))
if RECON == "wfuzz":
    print(wfuzz(URL))
if RECON == "spiderfoot":
    print(spiderfoot_modules(URL,ARGUMENTOS))
if RECON == "dirsearch":
    print(dirsearch_module(URL))
if RECON == "nikto":
    print(nikto_module(URL))
