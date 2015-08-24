#!/usr/bin/python
import smbus
import struct
import math

bus = smbus.SMBus(1)


class accelData:

    def __init__(self):
        self.Gx = 0
        self.Gy = 0
        self.Gz = 0
        self.Temp = 0
        self.Gyrox = 0
        self.Gyroy = 0
        self.Gyroz = 0


class mpu6050:

    AccelerationFactor = 2.0 / 32768.0
    GyroFactor = 500.0 / 32768.0
    TemperatureGain = 1.0 / 340.0
    TemperatureOffset = 36.53

    MPU6050_ADDRESS = 0x68
    MPU6050_RA_XG_OFFS_TC = 0x00
    MPU6050_RA_YG_OFFS_TC = 0x01
    MPU6050_RA_ZG_OFFS_TC = 0x02
    MPU6050_RA_X_FINE_GAIN = 0x03
    MPU6050_RA_Y_FINE_GAIN = 0x04
    MPU6050_RA_Z_FINE_GAIN = 0x05
    MPU6050_RA_XA_OFFS_H = 0x06
    MPU6050_RA_XA_OFFS_L_TC = 0x07
    MPU6050_RA_YA_OFFS_H = 0x08
    MPU6050_RA_YA_OFFS_L_TC = 0x09
    MPU6050_RA_ZA_OFFS_H = 0x0A
    MPU6050_RA_ZA_OFFS_L_TC = 0x0B
    MPU6050_RA_XG_OFFS_USRH = 0x13
    MPU6050_RA_XG_OFFS_USRL = 0x14
    MPU6050_RA_YG_OFFS_USRH = 0x15
    MPU6050_RA_YG_OFFS_USRL = 0x16
    MPU6050_RA_ZG_OFFS_USRH = 0x17
    MPU6050_RA_ZG_OFFS_USRL = 0x18
    MPU6050_RA_SMPLRT_DIV = 0x19
    MPU6050_RA_CONFIG = 0x1A
    MPU6050_RA_GYRO_CONFIG = 0x1B
    MPU6050_RA_ACCEL_CONFIG = 0x1C
    MPU6050_RA_FF_THR = 0x1D
    MPU6050_RA_FF_DUR = 0x1E
    MPU6050_RA_MOT_THR = 0x1F
    MPU6050_RA_MOT_DUR = 0x20
    MPU6050_RA_ZRMOT_THR = 0x21
    MPU6050_RA_ZRMOT_DUR = 0x22
    MPU6050_RA_FIFO_EN = 0x23
    MPU6050_RA_I2C_MST_CTRL = 0x24
    MPU6050_RA_I2C_SLV0_ADDR = 0x25
    MPU6050_RA_I2C_SLV0_REG = 0x26
    MPU6050_RA_I2C_SLV0_CTRL = 0x27
    MPU6050_RA_I2C_SLV1_ADDR = 0x28
    MPU6050_RA_I2C_SLV1_REG = 0x29
    MPU6050_RA_I2C_SLV1_CTRL = 0x2A
    MPU6050_RA_I2C_SLV2_ADDR = 0x2B
    MPU6050_RA_I2C_SLV2_REG = 0x2C
    MPU6050_RA_I2C_SLV2_CTRL = 0x2D
    MPU6050_RA_I2C_SLV3_ADDR = 0x2E
    MPU6050_RA_I2C_SLV3_REG = 0x2F
    MPU6050_RA_I2C_SLV3_CTRL = 0x30
    MPU6050_RA_I2C_SLV4_ADDR = 0x31
    MPU6050_RA_I2C_SLV4_REG = 0x32
    MPU6050_RA_I2C_SLV4_DO = 0x33
    MPU6050_RA_I2C_SLV4_CTRL = 0x34
    MPU6050_RA_I2C_SLV4_DI = 0x35
    MPU6050_RA_I2C_MST_STATUS = 0x36
    MPU6050_RA_INT_PIN_CFG = 0x37
    MPU6050_RA_INT_ENABLE = 0x38
    MPU6050_RA_DMP_INT_STATUS = 0x39
    MPU6050_RA_INT_STATUS = 0x3A
    MPU6050_RA_ACCEL_XOUT_H = 0x3B
    MPU6050_RA_ACCEL_XOUT_L = 0x3C
    MPU6050_RA_ACCEL_YOUT_H = 0x3D
    MPU6050_RA_ACCEL_YOUT_L = 0x3E
    MPU6050_RA_ACCEL_ZOUT_H = 0x3F
    MPU6050_RA_ACCEL_ZOUT_L = 0x40
    MPU6050_RA_TEMP_OUT_H = 0x41
    MPU6050_RA_TEMP_OUT_L = 0x42
    MPU6050_RA_GYRO_XOUT_H = 0x43
    MPU6050_RA_GYRO_XOUT_L = 0x44
    MPU6050_RA_GYRO_YOUT_H = 0x45
    MPU6050_RA_GYRO_YOUT_L = 0x46
    MPU6050_RA_GYRO_ZOUT_H = 0x47
    MPU6050_RA_GYRO_ZOUT_L = 0x48
    MPU6050_RA_EXT_SENS_DATA_00 = 0x49
    MPU6050_RA_EXT_SENS_DATA_01 = 0x4A
    MPU6050_RA_EXT_SENS_DATA_02 = 0x4B
    MPU6050_RA_EXT_SENS_DATA_03 = 0x4C
    MPU6050_RA_EXT_SENS_DATA_04 = 0x4D
    MPU6050_RA_EXT_SENS_DATA_05 = 0x4E
    MPU6050_RA_EXT_SENS_DATA_06 = 0x4F
    MPU6050_RA_EXT_SENS_DATA_07 = 0x50
    MPU6050_RA_EXT_SENS_DATA_08 = 0x51
    MPU6050_RA_EXT_SENS_DATA_09 = 0x52
    MPU6050_RA_EXT_SENS_DATA_10 = 0x53
    MPU6050_RA_EXT_SENS_DATA_11 = 0x54
    MPU6050_RA_EXT_SENS_DATA_12 = 0x55
    MPU6050_RA_EXT_SENS_DATA_13 = 0x56
    MPU6050_RA_EXT_SENS_DATA_14 = 0x57
    MPU6050_RA_EXT_SENS_DATA_15 = 0x58
    MPU6050_RA_EXT_SENS_DATA_16 = 0x59
    MPU6050_RA_EXT_SENS_DATA_17 = 0x5A
    MPU6050_RA_EXT_SENS_DATA_18 = 0x5B
    MPU6050_RA_EXT_SENS_DATA_19 = 0x5C
    MPU6050_RA_EXT_SENS_DATA_20 = 0x5D
    MPU6050_RA_EXT_SENS_DATA_21 = 0x5E
    MPU6050_RA_EXT_SENS_DATA_22 = 0x5F
    MPU6050_RA_EXT_SENS_DATA_23 = 0x60
    MPU6050_RA_MOT_DETECT_STATUS = 0x61
    MPU6050_RA_I2C_SLV0_DO = 0x63
    MPU6050_RA_I2C_SLV1_DO = 0x64
    MPU6050_RA_I2C_SLV2_DO = 0x65
    MPU6050_RA_I2C_SLV3_DO = 0x66
    MPU6050_RA_I2C_MST_DELAY_CTRL = 0x67
    MPU6050_RA_SIGNAL_PATH_RESET = 0x68
    MPU6050_RA_MOT_DETECT_CTRL = 0x69
    MPU6050_RA_USER_CTRL = 0x6A
    MPU6050_RA_PWR_MGMT_1 = 0x6B
    MPU6050_RA_PWR_MGMT_2 = 0x6C
    MPU6050_RA_BANK_SEL = 0x6D
    MPU6050_RA_MEM_START_ADDR = 0x6E
    MPU6050_RA_MEM_R_W = 0x6F
    MPU6050_RA_DMP_CFG_1 = 0x70
    MPU6050_RA_DMP_CFG_2 = 0x71
    MPU6050_RA_FIFO_COUNTH = 0x72
    MPU6050_RA_FIFO_COUNTL = 0x73
    MPU6050_RA_FIFO_R_W = 0x74
    MPU6050_RA_WHO_AM_I = 0x75

    ZeroRegister = [
        MPU6050_RA_FF_THR,
        MPU6050_RA_FF_DUR,
        MPU6050_RA_MOT_THR,
        MPU6050_RA_MOT_DUR,
        MPU6050_RA_ZRMOT_THR,
        MPU6050_RA_ZRMOT_DUR,
        MPU6050_RA_FIFO_EN,
        MPU6050_RA_I2C_MST_CTRL,
        MPU6050_RA_I2C_SLV0_ADDR,
        MPU6050_RA_I2C_SLV0_REG,
        MPU6050_RA_I2C_SLV0_CTRL,
        MPU6050_RA_I2C_SLV1_ADDR,
        MPU6050_RA_I2C_SLV1_REG,
        MPU6050_RA_I2C_SLV1_CTRL,
        MPU6050_RA_I2C_SLV2_ADDR,
        MPU6050_RA_I2C_SLV2_REG,
        MPU6050_RA_I2C_SLV2_CTRL,
        MPU6050_RA_I2C_SLV3_ADDR,
        MPU6050_RA_I2C_SLV3_REG,
        MPU6050_RA_I2C_SLV3_CTRL,
        MPU6050_RA_I2C_SLV4_ADDR,
        MPU6050_RA_I2C_SLV4_REG,
        MPU6050_RA_I2C_SLV4_DO,
        MPU6050_RA_I2C_SLV4_CTRL,
        MPU6050_RA_I2C_SLV4_DI,
        MPU6050_RA_INT_PIN_CFG,
        MPU6050_RA_INT_ENABLE,
        MPU6050_RA_I2C_SLV0_DO,
        MPU6050_RA_I2C_SLV1_DO,
        MPU6050_RA_I2C_SLV2_DO,
        MPU6050_RA_I2C_SLV3_DO,
        MPU6050_RA_I2C_MST_DELAY_CTRL,
        MPU6050_RA_SIGNAL_PATH_RESET,
        MPU6050_RA_MOT_DETECT_CTRL,
        MPU6050_RA_USER_CTRL,
        MPU6050_RA_CONFIG,
        MPU6050_RA_FF_THR,
        MPU6050_RA_FF_DUR,
        MPU6050_RA_MOT_THR,
        MPU6050_RA_MOT_DUR,
        MPU6050_RA_ZRMOT_THR,
        MPU6050_RA_ZRMOT_DUR,
        MPU6050_RA_FIFO_EN,
        MPU6050_RA_I2C_MST_CTRL,
        MPU6050_RA_I2C_SLV0_ADDR,
        MPU6050_RA_I2C_SLV0_REG,
        MPU6050_RA_I2C_SLV0_CTRL,
        MPU6050_RA_I2C_SLV1_ADDR,
        MPU6050_RA_I2C_SLV1_REG,
        MPU6050_RA_I2C_SLV1_CTRL,
        MPU6050_RA_I2C_SLV2_ADDR,
        MPU6050_RA_I2C_SLV2_REG,
        MPU6050_RA_I2C_SLV2_CTRL,
        MPU6050_RA_I2C_SLV3_ADDR,
        MPU6050_RA_I2C_SLV3_REG,
        MPU6050_RA_I2C_SLV3_CTRL,
        MPU6050_RA_I2C_SLV4_ADDR,
        MPU6050_RA_I2C_SLV4_REG,
        MPU6050_RA_I2C_SLV4_DO,
        MPU6050_RA_I2C_SLV4_CTRL,
        MPU6050_RA_I2C_SLV4_DI,
        MPU6050_RA_I2C_SLV0_DO,
        MPU6050_RA_I2C_SLV1_DO,
        MPU6050_RA_I2C_SLV2_DO,
        MPU6050_RA_I2C_SLV3_DO,
        MPU6050_RA_I2C_MST_DELAY_CTRL,
        MPU6050_RA_SIGNAL_PATH_RESET,
        MPU6050_RA_MOT_DETECT_CTRL,
        MPU6050_RA_USER_CTRL,
        MPU6050_RA_INT_PIN_CFG,
        MPU6050_RA_INT_ENABLE,
        MPU6050_RA_FIFO_R_W]

    def setup(self):
        self.setSampleRate(1000)
        self.setGResolution(2)
        bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_GYRO_CONFIG, 0b00001000)
        for loop in self.ZeroRegister:
            bus.write_byte_data(self.MPU6050_ADDRESS, loop, 0)
        bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_PWR_MGMT_1, 0b00000010)
        bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_PWR_MGMT_2, 0x00)
        bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_INT_ENABLE, 0x01)

    def __init__(self):
        self.setup()
        self.readStatus()
        self.fifoCount = 0

    def readDataFromFifo(self):
        while True:
            if self.fifoCount == 0:
                self.fifoCount = self.readFifoCount()
            if (self.fifoCount > 28):
                nCount = 28
            else:
                nCount = self.fifoCount
            GData = bus.read_i2c_block_data(self.MPU6050_ADDRESS, self.MPU6050_RA_FIFO_R_W, nCount)
            self.fifoCount = self.fifoCount - nCount
            return GData

    def readData(self):
        GData = bus.read_i2c_block_data(self.MPU6050_ADDRESS, self.MPU6050_RA_ACCEL_XOUT_H, 14)
        return self.convertData(GData)

    def convertData(self, ListData):
        ShortData = struct.unpack(">hhhhhhh", buffer(bytearray(ListData)))
        AccData = accelData()
        AccData.Gx = ShortData[0] * self.AccelerationFactor
        AccData.Gy = ShortData[1] * self.AccelerationFactor
        AccData.Gz = ShortData[2] * self.AccelerationFactor
        AccData.Temperature = ShortData[3] * self.TemperatureGain + self.TemperatureOffset
        AccData.Gyrox = ShortData[4] * self.GyroFactor
        AccData.Gyroy = ShortData[5] * self.GyroFactor
        AccData.Gyroz = ShortData[6] * self.GyroFactor
        return AccData

    def setGResolution(self, value):
        bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_GYRO_CONFIG, {2: 0, 4: 8, 8: 16, 16: 24}[value])
        self.AccelerationFactor = value / 32768.0

    def setSampleRate(self, Rate):
        SampleReg = int((8000 / Rate) - 1)
        self.SampleRate = 8000.0 / (SampleReg + 1.0)
        bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_SMPLRT_DIV, SampleReg)

    def readStatus(self):
        return  bus.read_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_INT_STATUS)

    def readFifoCount(self):
        GData = bus.read_i2c_block_data(self.MPU6050_ADDRESS, self.MPU6050_RA_FIFO_COUNTH)
        self.fifoCount = (GData[0] * 256 + GData[1])
        return self.fifoCount

    def readFifo(self, ByteCount):
        GData = bus.read_i2c_block_data(self.MPU6050_ADDRESS, self.MPU6050_RA_FIFO_R_W, ByteCount)
        return GData

    def resetFifo(self):
        bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_USER_CTRL, 0b00000000)
        pass
        bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_USER_CTRL, 0b00000100)
        pass
        bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_USER_CTRL, 0b01000000)

    def enableFifo(self, flag):
        bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_FIFO_EN, 0)
        if flag:
            self.resetFifo()
            bus.write_byte_data(self.MPU6050_ADDRESS, self.MPU6050_RA_FIFO_EN, 0b11111000)