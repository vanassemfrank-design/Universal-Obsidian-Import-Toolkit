from typing import Protocol


class Processor(Protocol):
    def process(self, item: object) -> object:
        ...