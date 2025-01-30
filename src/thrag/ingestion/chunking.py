from time import sleep
from typing import List

import structlog
from rich.progress import Progress

from thrag.ingestion.models import Chunk, Section

logger = structlog.get_logger(__name__)


def chunk_text(
    sections: List[Section],
    progress: Progress,
) -> List[Chunk]:
    """
    Placeholder: chunk each section into smaller pieces.
    """
    task_id = progress.add_task("Chunking text", total=len(sections))
    logger.debug("chunk_text.start", section_count=len(sections))

    chunks: List[Chunk] = []
    for i, sec in enumerate(sections):
        sleep(0.3)  # simulate
        # Dummy: just one chunk per section
        chunk = Chunk(content=sec.content[:100], section_index=i)
        chunks.append(chunk)
        progress.update(task_id, advance=1)

    progress.update(task_id, visible=False)
    logger.debug("chunk_text.end", chunk_count=len(chunks))
    return chunks
