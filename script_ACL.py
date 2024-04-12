aclNum = int(input("¿Cuál es el número ACL de IPv4? "))
if aclNum >= 1 and aclNum <= 99:
     print("Ésta es una ACL IPv4 estándar y le corresponde permit any.")
elif aclNum >=100 and aclNum <= 199:
     print("Esta es una ACL IPv4 extendida y le corresponde permit ip any any .")
else:
     print("Esta no es una ACL IPv4 estándar o extendida .")