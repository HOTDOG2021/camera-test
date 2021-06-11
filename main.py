import asyncio
from camera import capture
loop = asyncio.get_event_loop()

counter = 0
try:
    loop.run_until_complete(capture((2592,1944), counter))
    counter += 1
finally:
    loop.close()

