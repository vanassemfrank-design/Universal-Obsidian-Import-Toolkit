from unobit.core.context import PipelineContext
from unobit.resolvers.base import Resolver


class ResolutionStep:

    def __init__(self, resolvers: list[Resolver]):
        self.resolvers = resolvers

    def run(self, items, context: PipelineContext):

        current = list(items)

        for resolver in self.resolvers:
            current = resolver.resolve(current, context)

        return current