import magic
import glob
import hashlib
filenames = glob.glob("Dokaz_3/*")

for filename in filenames:
    with open(filename, "rb") as inputfile:
        data = inputfile.read()
        print("MD5:", hashlib.md5(data).hexdigest())
        print("SHA1:", hashlib.sha1(data).hexdigest())
        print("SHA256:", hashlib.sha256(data).hexdigest())
