from Crypto.Cipher import AES
import base64
from django.db import models
from cryptography.fernet import Fernet

class AesField(models.TextField):
    PADDING = '{'
    block_size = 16
    secret = 'this_is_secret'
    def __init__(self, *args, **kwargs):
        self.coder = kwargs.pop("coder", None)
        self.secret = self.pad(self.secret)
        self.cipher = AES.new(self.secret)

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def to_python(self, value):
        # 取数据时解密
        return self.decode(value)

    def get_prep_value(self, value):
        # 存数据时加密
        if not value:
            return value
        if not isinstance(value, str):
            value = str(value)
        return self.encode(value)

    def pad(self, s):
        return s + (self.block_size - len(s) % self.block_size) * self.PADDING

# from cryptography.fernet import Fernet
# key = Fernet.generate_key()
# cipher_suite = Fernet(key)
# cipher_text = cipher_suite.encrypt(b"A really secret message. Not for prying eyes.")
# plain_text = cipher_suite.decrypt(cipher_text)
# print(plain_text)
