import socket
import argparse
import ipaddress


parser = argparse.ArgumentParser(
                    prog='PortScanner',
                    description='Program to scan open ports using socket',
                    epilog='help')

parser.add_argument('-u')
parser.add_argument('-p', '--port')

args = parser.parse_args()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def portScan(ip, port):
    print(f"[ - ] Executando um scanner e portas simples na porta args.p")
    s.connect((ip, port))
    s.recv(1024)
    s.close()


portScan(args.u, args.port)
