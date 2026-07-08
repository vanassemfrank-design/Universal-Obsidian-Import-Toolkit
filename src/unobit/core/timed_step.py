from collections.abc import Iterable
from time import perf_counter

from unobit.core.context import PipelineContext


class TimedStep:
    def __init__(self, name: str, step: object) -> None:
        self.name = name
        self.step = step

    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        start = perf_counter()

        result = list(self.step.run(items, context))

        elapsed = perf_counter() - start
        context.report.add_timing(self.name, elapsed)

        return result