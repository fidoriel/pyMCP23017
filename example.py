import pyMCP23017
from time import sleep

# constructor
mcp = pyMCP23017.MCP23017(0x20)

# setup
pin=15
mcp.setup(pin, mcp.OUT)
# turn pin on
mcp.output(pin, mcp.HIGH)
sleep(1)
pin2=5
mcp.setup(pin2, mcp.OUT)
# turn pin on
mcp.output(pin2, mcp.HIGH)
sleep(1)
# turn pin off
mcp.output(pin2, mcp.LOW)
mcp.output(pin, mcp.LOW)

pin3 = 0
mcp.setup(pin3, mcp.IN, pull_up_down = mcp.PUD_UP)

# read pin3
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
