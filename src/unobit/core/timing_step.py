from collections.abc import Iterable
from time import perf_counter

from unobit.core.context import PipelineContext


class TimingStep:
    def __init__(self, name: str) -> None:
        self.name = name

    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        start = perf_counter()

        try:
            for item in items:
                yield item
        finally:
            elapsed = perf_counter() - start
            context.report.add_timing(self.name, elapsed)