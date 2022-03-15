import argparse
import asyncio
import time

import aiofiles
import aiohttp

URL = 'https://thisartworkdoesnotexist.com'
N = 0


async def main():
    async with aiohttp.ClientSession() as session:
        for i in range(N):
            async with session.get(URL) as response:
                async with aiofiles.open(f"artifacts/easy/image_{i + 1}.png", "bw") as file:
                    await file.write((await response.content.read()))
            if i != N - 1:
                time.sleep(1)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('n', type=int)
    args = parser.parse_args()
    N = args.n
    asyncio.run(main())
