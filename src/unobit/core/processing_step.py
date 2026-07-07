from collections.abc import Iterable

from unobit.core.context import PipelineContext
from unobit.processors.base import Processor


class ProcessingStep:
    def __init__(self, processors: list[Processor]) -> None:
        self.processors = processors

    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        for item in items:
            current = item

            for processor in self.processors:
                current = processor.process(current)

            yield current