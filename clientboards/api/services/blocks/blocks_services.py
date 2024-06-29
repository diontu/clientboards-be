import base64
import json


class BlockServices:
    @staticmethod
    def getBlocksByUserId(userId: int, blocksFilter: str | None = None) -> str:
        # decode the blocks filter (url encoded)
        if blocksFilter is not None:
            # return all blocks based on the filters
            pass
        else:
            # return all blocks for that specific user
            pass
        return 'blocks'
