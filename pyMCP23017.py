import smbus, sys, subprocess
from time import sleep

soc = 0
gpioSetup = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
gpioOut = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
gpioPullUp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
RgpioArowSet = 0x00
RgpioBrowSet = 0x01
RgpioArowOut = 0x12
RgpioBrowOut = 0x13
gppuA = 0x6
gppuB = 0x16

gpioAbinSet = ''
gpioBbinSet = ''

gpioAbinSetPu = ''
gpioBbinSetPu = ''

gpioAbinOut = ''
gpioBbinOut = ''

PUD_UP = 1

out = 0

class MCP23017:

    def __init__(self, adress):

        try:
            check = subprocess.check_output(['sudo i2cdetect -y 0'])
        except:
            soc = 1

        self.soc = soc
        self.adress = adress
        self.gpioSetup = gpioSetup
        self.gpioOut = gpioOut
        self.gpioPullUp = gpioPullUp

        self.gpioAbinSet = gpioAbinSet
        self.gpioBbinSet = gpioBbinSet

        self.gpioAbinSetPu = gpioAbinSetPu
        self.gpioBbinSetPu = gpioBbinSetPu

        self.gpioAbinOut = gpioAbinOut
        self.gpioBbinOut = gpioBbinOut

        self.IN = 1
        self.OUT = 0

        self.HIGH = 1
        self.LOW = 0

        self.PUD_UP = PUD_UP

        self.readArowStr = ''
        self.readBrowStr = ''

        self.readRowBin = []

        self.bus = smbus.SMBus(self.soc)

    def setup(self, pin, mode, pull_up_down = None):

        self.gpioAbinSet = ''
        self.gpioBbinSet = ''

        self.gpioSetup[pin] = mode

        for i in reversed(range(8)):
            self.gpioAbinSet += str(self.gpioSetup[i])
            self.gpioBbinSet += str(self.gpioSetup[i+8])

        self.bus.write_byte_data(self.adress, RgpioArowSet, int(self.gpioAbinSet, 2))
        self.bus.write_byte_data(self.adress, RgpioBrowSet, int(self.gpioBbinSet, 2))

        if pull_up_down != None:
            self._pullUp(pin, 1)
        else:
            self._pullUp(pin, 0)

        self.pull_up_down = None

    def output(self, pin, set):

        self.gpioAbinOut = ''
        self.gpioBbinOut = ''

        self.gpioOut[pin] = set

        for i in reversed(range(8)):
            self.gpioAbinOut += str(self.gpioOut[i])
            self.gpioBbinOut += str(self.gpioOut[i+8])

        self.bus.write_byte_data(self.adress, RgpioArowOut, int(self.gpioAbinOut, 2))
        self.bus.write_byte_data(self.adress, RgpioBrowOut, int(self.gpioBbinOut, 2))

    def input(self, pin):

        self.readArowStr = str(bin(self.bus.read_byte_data(self.adress, RgpioArowOut))[2:])
        self.readBrowStr = str(bin(self.bus.read_byte_data(self.adress, RgpioBrowOut))[2:])

        for y in reversed(self.readArowStr):
            self.readRowBin.append(int(y))

        for i in range(8-len(self.readRowBin)):
            self.readRowBin.append(0)

        for y in reversed(self.readBrowStr):
            self.readRowBin.append(int(y))

        for i in range(16-len(self.readRowBin)):
            self.readRowBin.append(0)

        return self.readRowBin[pin]

    def _pullUp(self, pin, up_down):

        self.gpioAbinSetPu = ''
        self.gpioBbinSetPu = ''

        self.gpioPullUp[pin] = up_down

        for i in reversed(range(8)):
            self.gpioAbinSetPu += str(self.gpioPullUp[i])
            self.gpioBbinSetPu += str(self.gpioPullUp[i+8])

        self.bus.write_byte_data(self.adress, gppuA, int(self.gpioAbinSetPu, 2))
        self.bus.write_byte_data(self.adress, gppuB, int(self.gpioBbinSetPu, 2))
