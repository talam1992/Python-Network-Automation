from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.64.72', 'timothy', 'cisco')
iosvl2.open()

ios_output = iosvl2.get_facts()
print(ios_output)