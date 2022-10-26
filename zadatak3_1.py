import asyncio
import time
import os

async def afun1(ls):
    time.sleep(0.2)
    for item in ls:
        file_size = os.path.getsize("D:/Faks/DisSys/DystSys-Zadace/" + item)
        return[{"naziv": item, "velicina": file_size} for item in ls]

def fun2(x):
    for item in x:
        with open(item["naziv"], "w") as fp:
            for i in range(10001): # off by one attitude
                fp.writelines(str(i) + " ")

async def main():
    lsDatoteka = []
    for i in range(3):
        name = "datoteka" + str(i+1) + ".txt"
        with open(name, "w") as fp:
            pass
    
    for file in os.listdir():
        if file.endswith(".txt"):
            lsDatoteka.append(file)

    lsOfDicts = await afun1(lsDatoteka)
    
    fun2(lsOfDicts)

    rez = await afun1(lsDatoteka)
    print(rez)


if __name__ == "__main__":
    asyncio.run(main())