
vlan1 = [10, 20, 30]
native_vlan1 = [99]
vlan2 = [40, 50, 60]
native_vlan2 = [200]

rp1 = int(input("lngresar la vlan lativa del SW1:"))
if rp1 == 99:
    print("la vlan es igual por lo cumplen con lo pedido")
else:
    print("la vlan no es igual y no cumplen con lo pedido")

rp2 = input("ingresar la vlan del SW1:")
rp2_list = list(map(int, rp2.split(',')))
if rp2_list == vlan1:
    print("la vlan es igual y cumplen con lo pedido")
else:
    print("la vlan no es igual y no cumplen con lo pedido")


rp3 = int(input("lngresar la vlan nativa del SW2:"))
if rp3 == 200:
    print("la vlan es igual y cumplen con lo pedido")
else:
    print("la vlan no es igual y no cumplen con lo pedido")


rp4 = input("ingresar la vlan del SW2:")
rp4_list = list(map(int, rp4.split(',')))
if rp4_list == vlan2:
    print("la vlan es igual y cumplen con lo pedido")
else:
    print("la vlan no es igual y no cumplen con lo pedido")