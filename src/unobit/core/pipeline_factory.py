from unobit.core.pipeline import ProcessingPipeline
from unobit.core.processing_step import ProcessingStep
from unobit.core.validation_step import ValidationStep
from unobit.processors.content_cleanup_processor import ContentCleanupProcessor
from unobit.processors.title_cleanup_processor import TitleCleanupProcessor
from unobit.validators.note_validator import NoteValidator
from unobit.validators.attachment_validator import AttachmentValidator
from unobit.validators.metadata_validator import MetadataValidator


class PipelineFactory:
    @staticmethod
    def create_default() -> ProcessingPipeline:
        return ProcessingPipeline(
            steps=[
                ValidationStep(
                    validators=[
                        NoteValidator(),
                        AttachmentValidator(),
                        MetadataValidator(),
                ]
            ),
                ProcessingStep(
                    processors=[
                        TitleCleanupProcessor(),
                        ContentCleanupProcessor(),
                    ]
                ),
            ]
        )