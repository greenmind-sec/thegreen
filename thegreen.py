import docker


VERSION = "0.1"
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

def google_hacking_search(alvo):
    image="greenmind/google_hacking_search:1"
    container = client.containers.run(image, alvo)
    saida=container.decode("utf-8")
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

# Função PDF
#TODO
#def GeneratePDF(output,name_output):
#    try:
#        pdf = canvas.Canvas('{}.pdf'.format(name_output))
#        x = 786
#        pdf.setTitle(name_output)
#        pdf.setFont("Helvetica-Oblique", 14)
#        pdf.drawString(245,750, 'TheGreen - Relatorio')
#        pdf.setFont("Helvetica-Bold", 12)
#        pdf.drawString(245,724, 'Whois IP')
#        for saida in output.items():
#            print(saida)
            #x -= 20
            #pdf.drawString(247,x, '{}'.format(saida))
        #pdf.drawString(245,786, output)
#        pdf.save()
#        print('{}.pdf criado com sucesso!'.format(name_output))
#    except:
#        print('Erro ao gerar {}.pdf'.format(name_output))

# Check root
if os.geteuid() != 0:
    print("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")
    sys.exit()
else:
    parser = argparse.ArgumentParser(description = 'GreenMind Security Scan.')

    #parser.add_argument('-t', action = 'store', dest = 'tipo', required = False,help = 'insert type.')
    parser.add_argument('-u', action = 'store', dest = 'url', required = True,help = 'insert target.')
    #parser.add_argument('-o', action = 'store', dest = 'save', required = False,help = 'save output file.')
    #parser.add_argument('-e', action = 'store', dest = 'email', required = False,help = 'search the email.')

    arguments = parser.parse_args()
    #TYPE=arguments.tipo
    URL = arguments.url
    #SAVE=arguments.save
    #EMAIL=arguments.email

    client = docker.from_env()

    # --------------------
    # Check info whois IP
    # --------------------
    print(whois_ip(URL))

    # --------------------
    # Check info whois URL
    # --------------------
    print(whois_url(URL))

    # --------------------
    # Check DNSlookup
    # --------------------
    print(dnslookup(URL))

    # --------------------
    # Check sharingmyip
    # --------------------
    print(sharingmyip(URL))

    # --------------------
    # Check Crt.sh
    # --------------------
    print(crt_sh(URL))
