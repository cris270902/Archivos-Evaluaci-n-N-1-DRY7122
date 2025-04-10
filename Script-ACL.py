#hola
acl = int(input("Ingrese numero de ACL IPV4: ")) 

if 1 <= acl <= 99 or 1300 <= acl <= 1999:
    print("ACL Estándar") 
elif 100 <= acl <= 199 or 2000 <= acl <= 2699:
    print("ACL Extendida")
else:
    print("Numero no corresponde a una ACL IPV4 valida")
