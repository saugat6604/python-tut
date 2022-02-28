from cryptography.fernet import Fernet



'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)'''

#write_key()
def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key


master_pwd = input("What is the master password? ")
key = load_key() + master_pwd.encode()
fer = Fernet(key)


def view():
    with open('Passwords.txt', 'r') as f:
        for line in f.readlines():
            #print(line.rstrip())
            data = line.rstrip()
            user, passw = data.split("|")
            #user=saugat passw=1234 aauxa split from |
            print("User:",user,"Password:",fer.decrypt(passw.encode()).decode())

        

def add():
    name = input('Account Name:')
    pwd = input("Password:")
    
    #with automatically close the file else we have to use file =open and file.close
    with open('Passwords.txt', 'a') as f:
        f.write(name + "|"+  fer.encrypt(pwd.encode()).decode()+"\n")



while True:
    mode = input("Would you like to add a new password or view existing password?Type view or add or q for exit ").lower()
    
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
         print("invalid mode ")



