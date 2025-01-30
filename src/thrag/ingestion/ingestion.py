from typing import List, Tuple

import structlog
from rich.progress import Progress

from thrag.ingestion.chunking import chunk_text
from thrag.ingestion.models import Chunk, Section
from thrag.ingestion.pdf_processing import extract_pdf_images, parse_images_to_elements
from thrag.ingestion.sectioning import semantic_sectioning

logger = structlog.get_logger(__name__)


def ingest_document(pdf_path: str, progress: Progress, config: dict) -> Tuple[List[Section], List[Chunk]]:
    """
    High-level pipeline to ingest a PDF, parse it, do semantic sectioning, chunking, etc.
    Using placeholders for actual logic.

    :param pdf_path: Path to the PDF file
    :param progress: Rich Progress instance for sub-tasks
    :param config: e.g. { "fallback_plan": [...], "some_other_config": ...}
    """
    logger.info("ingestion.start", pdf_path=pdf_path)

    # Step 1: Extract images
    image_paths = extract_pdf_images(pdf_path)

    # Step 2: Parse images with fallback
    elements = parse_images_to_elements(
        image_paths, progress=progress, fallback_plan=config.get("fallback_plan", [])
    )

    # Step 3: Sectioning
    sections = semantic_sectioning(elements, progress=progress)

    # Step 4: Chunking
    chunks = chunk_text(sections, progress=progress)

    logger.info(
        "ingestion.end",
        pdf_path=pdf_path,
        section_count=len(sections),
        chunk_count=len(chunks),
    )
    return sections, chunks
