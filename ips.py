import ipaddress

# com o ipaddress pode somar ips, fazer cálculo de ips e máscara de rede

# ip = '192.168.0.1'
# 
# endereco = ipaddress.ip_address(ip)
# 
# print(endereco)
# 
# print(endereco + 2000)

ip = '192.168.0.100/24'

rede = ipaddress.ip_network(ip, strict=False)

# print(red)

for ip in rede:
    print(ip)
