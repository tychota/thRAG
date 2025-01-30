from typing import List, Tuple

import structlog

from thrag.ingestion.models import Chunk, Section

logger = structlog.get_logger(__name__)


def ingest_document(
    pdf_path: str,
    config: dict,
) -> Tuple[List[Section], List[Chunk]]:
    """
    High-level pipeline to ingest a PDF, parse it, do semantic sectioning, chunking, etc.

    :param pdf_path: Path to the PDF file
    :param kb_id: Knowledge base ID (if relevant)
    :param doc_id: Document ID (if relevant)
    :param config: Ingestion config object (to be defined) with relevant params
    :return: Tuple of (sections, chunks) or whatever final structure
    """
    logger.info("ingestion.start", pdf_path=pdf_path)

    # 1. Convert PDF to images
    page_image_paths = []  # call something like extract_pdf_images(...)  # noqa: F841

    # 2. Parse images -> Elements
    elements = []  # parse_images_to_elements(...)   # noqa: F841

    # 3. Possibly do fallback if elements are empty
    # fallback_if_needed(...)

    # 4. Section text
    sections, document_lines = [], []  # noqa: F841

    # 5. Chunk it
    chunks = []

    logger.info("ingestion.end", section_count=len(sections), chunk_count=len(chunks))
    return sections, chunks
