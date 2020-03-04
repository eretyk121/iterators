import hashlib

def hash_text(path):
    with open(path, encoding='utf-8') as text:
        for line in text:
            md5_line = hashlib.md5(line.encode())
            yield md5_line.hexdigest()

for one_line in hash_text('DE.txt'):
    print(one_line)