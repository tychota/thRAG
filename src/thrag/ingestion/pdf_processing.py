from time import sleep
from typing import List

import structlog
from rich.progress import Progress

logger = structlog.get_logger(__name__)


def extract_pdf_images(pdf_path: str) -> List[str]:
    """
    Placeholder: Convert a PDF to images (page_1.png, page_2.png, etc.) and return the paths.
    Currently returns dummy paths.
    """
    logger.debug("extract_pdf_images.start", pdf_path=pdf_path)
    # TODO: implement real PDF-to-image
    sleep(0.5)  # simulate
    image_paths = ["page_1.png", "page_2.png"]
    logger.debug("extract_pdf_images.end", pdf_path=pdf_path, pages=len(image_paths))
    return image_paths


def parse_images_to_elements(
    image_paths: List[str],
    progress: Progress,
    fallback_plan: List[dict],
) -> List[dict]:
    """
    Placeholder: Parse each image using a fallback plan (list of VLM configs).
    We simulate calling each fallback in sequence if needed.

    :param image_paths: List of page image file paths
    :param progress: Rich Progress instance for sub-progress
    :param fallback_plan: List of dict configs, e.g. [ {"provider":"vlm_1"}, {"provider":"human"} ]
    :return: List of parsed 'elements'
    """
    task_id = progress.add_task("Parsing pages", total=len(image_paths))
    all_elements = []

    for path in image_paths:
        logger.debug("parse_images_to_elements.page.start", page=path)
        success = False
        result = None
        # Attempt fallback
        for fallback_config in fallback_plan:
            # TODO: real attempt using fallback_config
            sleep(0.3)  # simulate
            # simulate success on second fallback
            if fallback_config.get("provider") == "human":
                result = {"type": "text", "content": f"Human-verified text from {path}"}
                success = True
                break
            # or you might fail the attempt with an exception
            # raise or continue

        if not success:
            logger.warning("parse_images_to_elements.page.failed", page=path)
            result = {"type": "error", "content": f"Failed to parse {path}"}

        all_elements.append(result)
        progress.update(task_id, advance=1)
        logger.debug("parse_images_to_elements.page.end", page=path, success=success)

    # Hide this sub-progress bar
    progress.update(task_id, visible=False)

    return all_elements
