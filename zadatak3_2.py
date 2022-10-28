import asyncio
import numpy
import psutil
import time

async def afunc1():
    # 10 n dist with 1milli samples
    mu, sigma = 0, 0.1
    numpy.random.normal(mu,sigma, 1000000)
    time.sleep(0.9)

async def afunc2():
    return(psutil.cpu_percent(10))

async def main():
    await afunc1()
    rez = await afunc2()

    print("Iskorištenost CPU-a u 10 sekundi: " + str(rez))

if __name__ == "__main__":
    asyncio.run(main())