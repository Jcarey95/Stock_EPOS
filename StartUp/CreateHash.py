import hashlib


def md5sum():
    f_name = open('Start_Up.py', mode='r')
    hash_code = hashlib.md5()
    for buf in f_name.read(128):
        hash_code.update(buf.encode())
    return hash_code.hexdigest()
print(md5sum())
