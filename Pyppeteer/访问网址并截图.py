import asyncio
from pyppeteer import launch

async def main():
    broeser = await launch()
    page = await broeser.newPage()
    await page.goto('https://www.baidu.com')
    await page.screenshot({'path':'example.png'})
    await broeser.close()

asyncio.get_event_loop().run_until_complete(main())