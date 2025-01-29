import logging
from time import sleep

import click
import structlog
from rich.console import Console
from rich.logging import RichHandler
from rich.progress import track

from thrag.log import configure_logging


def configure_console_logging(log_level=logging.INFO):
    """
    Configure structlog and Python logging to output to the console
    with a RichHandler for pretty logs.
    """
    logging.basicConfig(
        level=log_level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(rich_tracebacks=True)],
    )


logger = structlog.get_logger(__name__)
console = Console()


@click.command()
@click.option("--iterations", default=5, help="Number of iterations in the demo progress bar.")
@click.option("--debug", is_flag=True, help="Enable DEBUG logging.")
def main(iterations, debug):
    """
    Example CLI that demonstrates structlog + Rich progress bars.
    """
    # Configure logging level
    log_level = logging.DEBUG if debug else logging.INFO
    configure_logging(log_level=log_level)
    configure_console_logging(log_level=log_level)

    logger.info("cli.start", message="Starting the CLI demo", iterations=iterations)

    # Show a Rich progress bar
    console.log("Starting a small demo loop...")
    for i in track(range(iterations), description="Processing items..."):
        logger.debug("cli.loop_iteration", iteration=i)
        sleep(0.5)  # simulate some work

    logger.info("cli.end", message="CLI demo complete")
    console.log("[bold green]All done![/bold green]")


if __name__ == "__main__":
    # If using as a standalone script:
    main()  # click command
