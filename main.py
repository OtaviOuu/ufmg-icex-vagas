import asyncio
import aiohttp
from parsel.selector import Selector

# https://www.icex.ufmg.br/icex_novo/oportunidades/


async def get_job_links(session: aiohttp.ClientSession, html: str):
    doc = Selector(text=html)
    links = doc.css(".eael-timeline-post a::attr(href)").getall()

    return links


async def get_main_page(session: aiohttp.ClientSession):
    async with session.get(
        "https://www.icex.ufmg.br/icex_novo/oportunidades/"
    ) as response:
        html = await response.text()

        return html


async def main():
    async with aiohttp.ClientSession() as session:
        html = await get_main_page(session)
        await get_job_links(session, html)


if __name__ == "__main__":
    asyncio.run(main())
