from collections.abc import Iterable
from typing import Protocol

from unobit.core.context import PipelineContext


class PipelineStep(Protocol):
    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        ...


class ProcessingPipeline:
    def __init__(self, steps: list[PipelineStep] | None = None) -> None:
        self.steps = steps or []

    def add_step(self, step: PipelineStep) -> None:
        self.steps.append(step)

    def run(self, items: Iterable[object], context: PipelineContext) -> list[object]:
        current: Iterable[object] = items

        for step in self.steps:
            current = step.run(current, context)

        return list(current)
    
    def with_step(self, step: PipelineStep) -> "ProcessingPipeline":
        self.add_step(step)
        return self