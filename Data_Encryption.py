from cryptography.fernet import Fernet

def application_encrypt():
	key = Fernet.generate_key()

	with open('appkey.key', 'wb') as filekey:
		filekey.write(key)

	with open('appkey.key', 'rb') as filekey:
		key = filekey.read()

	fernet = Fernet(key)

	with open('Application_Log.csv', 'rb') as file:
		original = file.read()
		
	encrypted = fernet.encrypt(original)

	with open('Application_Log.csv', 'wb') as encrypted_file:
		encrypted_file.write(encrypted)

def security_encrypt():
	key = Fernet.generate_key()

	with open('securitykey.key', 'wb') as filekey:
		filekey.write(key)

	with open('securitykey.key', 'rb') as filekey:
		key = filekey.read()

	fernet = Fernet(key)

	with open('Security_Log.csv', 'rb') as file:
		original = file.read()
		
	encrypted = fernet.encrypt(original)

	with open('Security_Log.csv', 'wb') as encrypted_file:
		encrypted_file.write(encrypted)

def system_encrypt():
	key = Fernet.generate_key()

	with open('systemkey.key', 'wb') as filekey:
		filekey.write(key)

	with open('systemkey.key', 'rb') as filekey:
		key = filekey.read()

	fernet = Fernet(key)

	with open('System_Log.csv', 'rb') as file:
		original = file.read()
		
	encrypted = fernet.encrypt(original)

	with open('System_Log.csv', 'wb') as encrypted_file:
		encrypted_file.write(encrypted)	

application_encrypt()		
security_encrypt()
system_encrypt()