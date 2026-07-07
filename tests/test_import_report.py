from unobit.core.report import ImportReport


def test_import_report_counts_notes():
    report = ImportReport(
        source="samples/evernote/test.enex",
        importer="evernote",
    )

    report.notes_total += 1
    report.notes_success += 1
    report.finish()

    assert report.notes_total == 1
    assert report.notes_success == 1
    assert report.finished_at is not None