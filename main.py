import asyncio
from camera import capture

def main():
    loop = asyncio.get_event_loop()

    counter = 0
    try:
        loop.run_until_complete(capture((2592,1944), counter))
        counter += 1
    finally:
        loop.close()

if __name__ == "__main__":
    main()