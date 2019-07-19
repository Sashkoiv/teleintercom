from machine import Pin, I2C
import ds1307

def getTemp(addr, scl_pin = 5, sda_pin = 4):
    i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000)

    return float(i2c.readfrom(addr, 8)[0])

def show_config(addr, scl_pin = 5, sda_pin = 4):
    i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000)
    raw = i2c.readfrom(addr, 8)[3] & 0xFFF
    print ("{0:b} binary & {0:f} read from OS".format(raw))
    raw = i2c.readfrom(addr, 8)[2] & 0xFFF
    print ("{0:b} binary & {0:f} read from HYST".format(raw))

def readAsData(addr, scl_pin = 5, sda_pin = 4):
    i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000)
    raw = i2c.readfrom(addr, 8)
    for r in raw:
        print ("{0:b} binary & {0:f} dec".format(r & 0xFFF))

def readAllDev(scl_pin = 5, sda_pin = 4):
    i2c = I2C(scl=Pin(scl_pin), sda=Pin(sda_pin), freq=100000)
    for a in i2c.scan():
        raw = i2c.readfrom(a, 64)
        print('Device with address {0}'.format(a))
        for r in raw:
            print ("{0:b} binary & {0:f} dec".format(r & 0xFFFFF))

# if __name__ == "__main__":
#     i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)
#     ds = ds1307.DS1307(i2c)
#     print(ds.datetime())
    # print(ds.datetime())
    # ds.datetime(now)
    # getTemp(72, 5, 4)
    # readAllDev()
    # print(getTemp(72))