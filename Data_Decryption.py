from cryptography.fernet import Fernet

def application_decrypt():
	with open('appkey.key', 'rb') as filekey:
		key = filekey.read()

	fernet = Fernet(key)

	with open('Application_Log.csv', 'rb') as enc_file:
		encrypted = enc_file.read()

	decrypted = fernet.decrypt(encrypted)

	with open('Application_Log.csv', 'wb') as dec_file:
		dec_file.write(decrypted)

def security_decrypt():
	with open('securitykey.key', 'rb') as filekey:
		key = filekey.read()

	fernet = Fernet(key)

	with open('Security_Log.csv', 'rb') as enc_file:
		encrypted = enc_file.read()

	decrypted = fernet.decrypt(encrypted)

	with open('Security_Log.csv', 'wb') as dec_file:
		dec_file.write(decrypted)

def system_decrypt():
	with open('systemkey.key', 'rb') as filekey:
		key = filekey.read()

	fernet = Fernet(key)

	with open('System_Log.csv', 'rb') as enc_file:
		encrypted = enc_file.read()

	decrypted = fernet.decrypt(encrypted)

	with open('System_Log.csv', 'wb') as dec_file:
		dec_file.write(decrypted)


application_decrypt()
security_decrypt()
system_decrypt()