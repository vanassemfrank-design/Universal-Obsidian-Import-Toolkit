from unobit.core.pipeline import ProcessingPipeline
from unobit.core.processing_step import ProcessingStep
from unobit.core.validation_step import ValidationStep
from unobit.validators.note_validator import NoteValidator


class PipelineFactory:
    @staticmethod
    def create_default() -> ProcessingPipeline:
        return ProcessingPipeline(
            steps=[
                ValidationStep(
                    validators=[
                        NoteValidator(),
                    ]
                ),
                ProcessingStep(
                    processors=[]
                ),
            ]
        )