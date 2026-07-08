from pathlib import Path

from unobit.core.context import PipelineContext
from unobit.core.pipeline_factory import PipelineFactory
from unobit.core.report import ImportReport
from unobit.models import Note


def test_default_pipeline_resolves_evernote_internal_links():
    report = ImportReport(source="test.enex", importer="evernote")

    context = PipelineContext(
        source_path=Path("test.enex"),
        output_path=Path("output"),
        importer_name="evernote",
        report=report,
    )

    target_guid = "11111111-1111-1111-1111-111111111111"

    source = Note(
        title=" Source Note ",
        source="evernote",
        body=f"\nZie [target](evernote:///view/123/abc/{target_guid}/{target_guid}/).\n",
        metadata={"guid": "22222222-2222-2222-2222-222222222222"},
    )

    target = Note(
        title="Target Note",
        source="evernote",
        body="Ik ben doel.",
        metadata={"guid": target_guid},
    )

    pipeline = PipelineFactory.create_default()
    result = pipeline.run([source, target], context)

    assert result[0].title == "Source Note"
    assert result[0].body.startswith("Zie")
    assert "[[Target Note|target]]" in result[0].body