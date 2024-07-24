def stream_chunks(ichunk):
    n_chunks = 0
    all_empty = True
    for chunk in ichunk:
        assert chunk.type == "AIMessageChunk"
        assert isinstance(chunk.content, str)
        all_empty &= len(chunk.content) == 0
        n_chunks += 1
        if n_chunks >= 5:
            break
    assert not all_empty


async def astream_chunks(async_ichunk):
    n_chunks = 0
    all_empty = True
    async for chunk in async_ichunk:
        assert chunk.type == "AIMessageChunk"
        assert isinstance(chunk.content, str)
        all_empty &= len(chunk.content) == 0
        n_chunks += 1
        if n_chunks >= 5:
            break
    assert not all_empty
