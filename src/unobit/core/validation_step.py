from collections.abc import Iterable

from unobit.core.context import PipelineContext
from unobit.validators.base import Validator


class ValidationStep:
    def __init__(self, validators: list[Validator]) -> None:
        self.validators = validators

    def run(self, items: Iterable[object], context: PipelineContext) -> Iterable[object]:
        for item in items:
            for validator in self.validators:
                result = validator.validate(item)

                for message in result.messages:
                    if message.level == "error":
                        context.report.add_error(
                            message.message,
                            code=message.code,
                            **(message.context or {}),
                        )
                    elif message.level == "warning":
                        context.report.add_warning(
                            message.message,
                            code=message.code,
                            **(message.context or {}),
                        )

            yield item