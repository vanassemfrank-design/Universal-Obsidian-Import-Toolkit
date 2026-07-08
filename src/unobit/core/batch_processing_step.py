from collections.abc import Iterable

from unobit.core.context import PipelineContext


class BatchProcessingStep:
    def __init__(self, processors: list[object]) -> None:
        self.processors = processors

    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        current = list(items)

        for processor in self.processors:
            current = processor.process_all(current, context)

        return current