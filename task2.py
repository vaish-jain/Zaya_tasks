#!/usr/bin/python3

from faker import Factory

def get_value(num, fake):
    print("Values are listed below:\n")
    for i in range(1,num):
        print("device-id =", fake.random_number())
        print("mac-address =", fake.mac_address())
        print("wifi-mac-address =", fake.md5(raw_output=False))

if __name__ == "__main__":
    num = int(input("Enter number of devices: "))
    fake_data = Factory.create()
    get_value(num,fake_data)


