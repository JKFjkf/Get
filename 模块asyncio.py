from datetime import datetime
import 模块asyncio



async def wait():
    模块asyncio.sleep(5)
    print("等我5秒")

async def print_time(word):
    print(word,datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

async def main():
    await print_time("开始")
    await wait()
    await print_time("结束")

loop = 模块asyncio.get_event_loop()
loop.run_unit_complete(main())
loop.close()