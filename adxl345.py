from machine import Pin, I2C
import time, ustruct

# Constantes ADXL345
ADXL345_I2C_ADDR   = 0x53        # dirección I²C del sensor
ADXL345_POWER_CTL  = 0x2D        # registro POWER_CTL
ADXL345_DATA_FMT   = 0x31        # registro DATA_FORMAT
ADXL345_DATAX0     = 0x32        # primer byte de datos X


def init_adxl345(i2c):
    # Modo Measurement (bit 3=1)
    i2c.writeto_mem(ADXL345_I2C_ADDR, ADXL345_POWER_CTL,  b'\x08')
    # Full-res ±16 g (bit 3=1, RANGE=3)
    i2c.writeto_mem(ADXL345_I2C_ADDR, ADXL345_DATA_FMT,   b'\x0B')

def read_accel(i2c):
    # Lee 6 bytes (X0,X1,Y0,Y1,Z0,Z1)
    data = i2c.readfrom_mem(ADXL345_I2C_ADDR, ADXL345_DATAX0, 6)
    x, y, z = ustruct.unpack('<3h', data)  # little-endian, signed
    # Convierte a g (LSB=0.0039 g)
    return x * 0.0039, y * 0.0039, z * 0.0039
