import asyncio
import re
from pyppeteer import launch

async def main():
    browser = await launch({'headless':False})
    page = await browser.newPage()
    await page.setViewport({'width':1200})
    await page.goto('https://www.phei.com.cn/module/goods/wssd_index.jsp')
    lis = await page.querySelectorAll('#book_sort_area  ul:nth-child(1)  li')
    for li in lis:
        image_element = await li.querySelector("p  a  img")
        image = await (await image_element.getProperty("src")).jsonValue()
        book_element = await li.querySelector()
        print([image])
    await page.waitForNavigation()

asyncio.get_event_loop().run_until_complete(main())