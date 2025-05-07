from machine import Pin, I2C
from adxl345 import init_adxl345, read_accel


# Inicializa I2C0 en GP0 (SDA) y GP1 (SCL) a 400 kHz
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)


# Arranque
init_adxl345(i2c)
while True:
    ax, ay, az = read_accel(i2c)
    print("X={:+.3f} g  Y={:+.3f} g  Z={:+.3f} g".format(ax, ay, az))
    time.sleep(0.1)
