from dataclasses import dataclass
from typing import List


@dataclass
class Result:
    words: List[str]


class ResultFactory:

    @staticmethod
    def create(data: List[dict]) -> Result:
        words = [item["text"] for item in data]
        return Result(words=words)
