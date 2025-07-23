import aiohttp


class AiohttpClient:
    session: aiohttp.ClientSession | None = None

    async def start(self) -> None:
        if self.session is None:
            self.session = aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=300.0))

    async def stop(self) -> None:
        if self.session is not None:
            await self.session.close()
            self.session = None

    def __call__(self) -> aiohttp.ClientSession:
        assert self.session is not None, "Session has not been started"
        return self.session


aiohttp_client = AiohttpClient()
