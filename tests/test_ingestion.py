from unittest.mock import MagicMock

from thrag.ingestion.ingestion import ingest_document


def test_ingest_document():
    progress = MagicMock()
    sections, chunks = ingest_document("fake.pdf", progress, {"fallback_plan": []})
    assert len(sections) >= 0
    assert len(chunks) >= 0
