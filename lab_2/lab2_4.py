import magic
import glob
import hashlib
filenames = glob.glob("Dokaz_4/*")
challenge = "c15e32d27635f248c1c8b66bb012850e5b342119"

for filename in filenames:
    with open(filename, "rb") as inputfile:
        data = inputfile.read()
        if hashlib.sha1(data).hexdigest() == challenge:
            print(filename, magic.from_file(filename))
            break

