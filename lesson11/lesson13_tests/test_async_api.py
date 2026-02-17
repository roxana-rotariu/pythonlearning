import pytest
import aiohttp
from unittest.mock import AsyncMock, patch

@pytest.mark.asyncio
async def test_async_api():
    # Creează un mock care poate fi folosit cu "async with"
    mock_response = AsyncMock()
    mock_response.__aenter__.return_value.status = 200
    mock_response.__aenter__.return_value.json = AsyncMock(return_value={"id": 5, "title": "async mocked"})

    with patch("aiohttp.ClientSession.get", return_value=mock_response):
        async with aiohttp.ClientSession() as session:
            async with session.get("https://jsonplaceholder.typicode.com/todos/1") as resp:
                assert resp.status == 200
                data = await resp.json()
                assert data["id"] == 5
                assert data["title"] == "async mocked"