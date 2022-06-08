# string = "[Device Install (Hardware initiated) - SWD\WPDBUSENUM\_??_USBSTOR#Disk&Ven_JetFlash&Prod_Transcend_16GB&Rev_1.00#3451413224&0#{53f56307-b6bf-11d0-94f2-00a0c91efb8b}]"

usb_counter = 1


def usb_info(string):
    print(string)
    print("Vendor: " + string.split("Ven_")[1].split("&Prod_")[0])
    print("Product: " + string.split("&Prod_")[1].split("&Rev_")[0])
    print("Serial: " + string.split("#")[2].split("#")[0])


with open("sy.txt") as f:
    for i in f:
        if i.find("Device Install (Hardware initiated)") != -1 and i.find("Ven_") != -1:
            # print(str(usb_counter) + i)
            print(str(usb_counter))
            usb_info(i)
            print(next(f))
            print("-"*165 + "\n")
            usb_counter += 1
