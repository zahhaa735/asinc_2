import asyncio
import aiohttp


async def fetch(session, url):
    async with session.get(url, ssl=False) as response:
        return await response.text()


async def search_keyword(url, keyword):
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, url)
        if keyword in html:
            print(f"Keyword '{keyword}' found on {url}")
        else:
            print(f"Keyword '{keyword}' not found on {url}")


async def main():
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]
    keyword = "python"

    tasks = []
    for url in urls:
        task = asyncio.create_task(search_keyword(url, keyword))
        tasks.append(task)

    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
