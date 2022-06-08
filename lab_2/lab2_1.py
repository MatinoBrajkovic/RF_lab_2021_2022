import magic
import glob
filenames = glob.glob("Dokaz_1/*")

for filename in filenames:
    print(filename, magic.from_file(filename))
    print(magic.from_buffer(open(filename, "rb").read(2048)))
# print(magic.from_file("Dokaz_1/file1"))
# print(magic.from_file("Dokaz_1/file2.txt"))
# print(magic.from_file("Dokaz_1/file3"))