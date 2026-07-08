from unobit.core.pipeline import ProcessingPipeline
from unobit.core.processing_step import ProcessingStep
from unobit.core.timed_step import TimedStep
from unobit.core.validation_step import ValidationStep
from unobit.processors.content_cleanup_processor import ContentCleanupProcessor
from unobit.processors.title_cleanup_processor import TitleCleanupProcessor
from unobit.validators.attachment_validator import AttachmentValidator
from unobit.validators.metadata_validator import MetadataValidator
from unobit.validators.note_validator import NoteValidator
from unobit.core.batch_processing_step import BatchProcessingStep
from unobit.processors.evernote_internal_link_processor import EvernoteInternalLinkProcessor
from unobit.core.resolution_step import ResolutionStep
from unobit.resolvers.evernote_links import EvernoteInternalLinkResolver

class PipelineFactory:
    @staticmethod
    def create_default() -> ProcessingPipeline:
        return ProcessingPipeline(
            steps=[
                TimedStep(
                    "validation",
                    ValidationStep(
                        validators=[
                            NoteValidator(),
                            AttachmentValidator(),
                            MetadataValidator(),
                        ]
                    ),
                ),
                TimedStep(
                    "processing",
                    ProcessingStep(
                        processors=[
                            TitleCleanupProcessor(),
                            ContentCleanupProcessor(),
                        ]
                    ),
                ),
                TimedStep(
                    "resolution",
                    ResolutionStep(
                        resolvers=[
                            EvernoteInternalLinkResolver(),
                        ]
                    ),
                ),
                TimedStep(
                    "evernote-links",
                    BatchProcessingStep(
                        processors=[
                            EvernoteInternalLinkProcessor(),
                        ]
                    ),
                ),
            ]
        )