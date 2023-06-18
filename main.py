import Log_Collector
import Selenium_Connection
import Data_Encryption
import Data_Decryption

#Generating Logs
print("\n System Logs ")
Log_Collector.system()
print("\n Security Logs ")
Log_Collector.security()
print("\n Application Logs ")
Log_Collector.application()

#Automation to upload files
Selenium_Connection.user_pass()
Selenium_Connection.connection()

#Encrypting the data
Data_Encryption.application_encrypt()
Data_Encryption.security_encrypt()
Data_Encryption.system_encrypt()

##Decrypting the data
#Data_Decryption.application_encrypt()
#Data_Decryption.security_encrypt()
#Data_Decryption.system_encrypt()