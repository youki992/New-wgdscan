import os
#author:Jaky

def xray(ip):
  name=ip.replace('https://', '').replace('http://', '').replace('/', '')
  exp=(("xray_windows_amd64.exe webscan --basic-crawler {0}/ --html-output {1}.html").format(ip,name))
  print('\nxray starting----------------------')
  os.system(exp)

if __name__ == "__main__":
  with open('ip.txt','r') as file: list = [www.strip() for www in file.readlines()]
  for ip in list: xray(ip)