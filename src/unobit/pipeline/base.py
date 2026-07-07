from abc import ABC, abstractmethod

from unobit.core.context import PipelineContext


class PipelineStep(ABC):

    @abstractmethod
    def run(self, notes, context: PipelineContext):
        ...