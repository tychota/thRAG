from unittest.mock import MagicMock

from thrag.ingestion.pdf_processing import extract_pdf_images, parse_images_to_elements


def test_extract_pdf_images():
    images = extract_pdf_images("fake.pdf")
    assert len(images) == 2


def test_parse_images_to_elements():
    progress = MagicMock()
    res = parse_images_to_elements(["page_1.png"], progress, [{"provider": "vlm_1"}])
    assert len(res) == 1
