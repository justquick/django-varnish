import telnetlib

url = '/sports/'

tn = telnetlib.Telnet('172.16.12.68',82)
tn.write("purge.url %s\n"%url)
assert tn.read_until('\n\n').startswith('200')