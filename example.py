import pyMCP23017
from time import sleep

mcp = pyMCP23017.MCP23017(0x20)

pin=15
mcp.setup(pin, mcp.OUT)
mcp.output(pin, mcp.HIGH)
sleep(1)
pin2=5
mcp.setup(pin2, mcp.OUT)
mcp.output(pin2, mcp.HIGH)
sleep(1)
mcp.output(pin2, mcp.LOW)
mcp.output(pin, mcp.LOW)

pin3 = 0
mcp.setup(pin3, mcp.IN, pull_up_down = mcp.PUD_UP)

if mcp.input(pin3):
    print('True')
else:
    print('False')

pin4 = 9
mcp.setup(pin4, mcp.IN)

if mcp.input(pin4):
    print('True')
else:
    print('False')
