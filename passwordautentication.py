import getpass

database={"david": "12345", "daniel": "91413376"}
username=input("enter your username: ")
password=getpass.getpass("enter your password: ")
for i in database.keys():
	if username== i:
		while password !=database.get(i):
			password=getpass.getpass("enter your password again: ")
		break
print("verified")


#por alguna razon este programa no funciona bien