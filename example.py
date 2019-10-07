import pyMCP23017
from time import sleep

mcp = pyMCP23017.MCP23017(0x20)

pin=15
mcp.setup(pin, mcp.OUT)
mcp.output(pin, mcp.HIGH)
sleep(1)
mcp.output(pin, mcp.LOW)

pin2 = 0
mcp.setup(pin2, mcp.IN, pull_up_down = mcp.PUD_UP)

if mcp.input(pin2):
    print('True')
else:
    print('False')
