import re

usb_counter = 1

vendor_regex = "Ven_(.*)&Prod_"
product_regex = "Prod_(.*)(&Rev_|_#)"
serial_regex = ".*#.*#(.*)#.*"


def usb_info_regex(string):
    print(string)
    print("Vendor: " + re.search(vendor_regex, string).group(1))
    print("Product: " + re.search(product_regex, string).group(1))
    print("Serial: " + re.search(serial_regex, string).group(1))


with open("sy.txt") as f:
    for i in f:
        if i.find("Device Install (Hardware initiated)") != -1 and i.find("Ven_") != -1:
            print(str(usb_counter))
            usb_info_regex(i)
            print(next(f))
            print("-"*200 + "\n")
            usb_counter += 1
