from cryptography.fernet import Fernet
key = Fernet.generate_key()
print(key)


from cryptography.fernet import Fernet
#key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='
key = b'Iixkr_C_Q8XbU3FoqfIgshj9d-Vnf3-cUMa9ThzwY-8='
cipher_suite = Fernet(key)
ciphered_text = cipher_suite.encrypt(b'J0J0BizarreAD')   #required to be bytes
print(ciphered_text)


#ciphered_text = b'gAAAAABaHvk3g8IG4cln7g5HCulppy1bAPVuhtskVcgPXRyytx6RkIqjcI0mAMA7Oy_56T6J0dk-yjxI_WlZtjxnUBbR-EvoQa_oqCKoQJFbv_uc2WdXMSI='
#key = b'pRmgMa8T0INjEAfksaq2aafzoZXEuwKI7wDe4c1F8AY='


from cryptography.fernet import Fernet
def pw_decrypter():
    key = b'Iixkr_C_Q8XbU3FoqfIgshj9d-Vnf3-cUMa9ThzwY-8='
    cipher_suite = Fernet(key)
    ciphered_text = b'gAAAAABd_S9TcWwZw0UpRH_GLHWd8KNcLLkmfLD-1-U1E0_XKqOeyB4Z8sIvvAXO27x4DmW79QZL4RteX6F8OQJLBR89jDCJjQ=='
    unciphered_text = (cipher_suite.decrypt(ciphered_text))
    pwd = str(unciphered_text)[2:15]
    return pwd

print(unciphered_text)
