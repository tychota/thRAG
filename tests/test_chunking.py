from unittest.mock import MagicMock

from thrag.ingestion.chunking import chunk_text
from thrag.ingestion.models import Section


def test_chunk_text():
    sections = [Section(title="Test", content="Long text...")]
    progress = MagicMock()
    chunks = chunk_text(sections, progress=progress)
    assert len(chunks) == 1
