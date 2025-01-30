from unittest.mock import MagicMock

from thrag.ingestion.sectioning import semantic_sectioning


def test_semantic_sectioning():
    elements = [{"type": "text", "content": "Hello World"}]
    progress = MagicMock()
    res = semantic_sectioning(elements, progress=progress)
    assert len(res) == 1
