import asyncio


async  def start_strongman(name, power):
    print(f'Силач {name} начал соревнования.')
    for i in range(1,6):
        await asyncio.sleep(1 / power)
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    strongman_1 = asyncio.create_task(start_strongman('Pasha', 3))
    strongman_2 = asyncio.create_task(start_strongman('Denis', 4))
    strongman_3 = asyncio.create_task(start_strongman('Apollon', 5))
    await strongman_1
    await strongman_2
    await strongman_3


asyncio.run(start_tournament())

