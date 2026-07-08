from typing import Protocol

from unobit.core.context import PipelineContext


class Resolver(Protocol):

    def resolve(
        self,
        items: list[object],
        context: PipelineContext,
    ) -> list[object]:
        ...