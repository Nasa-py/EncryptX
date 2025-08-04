from cryptography.fernet import Fernet

a = input("enter the file that u want to encrypt: ".title())
def encryption():
    with open(f"{a}.txt","r")as file:
        b = file.read()
        print (b)

    with open("encry.txt","w") as file:
        key = Fernet.generate_key()
        f = Fernet(key)
        t = f.encrypt(b.encode())
        file.write(str(t))
    h = input("enter the file that u want to decrypte: ".title())
    with open (f"{h}.txt","w")as file:
        to=f.decrypt(t)
        file.write(str(to))
g = encryption()
print (g)
