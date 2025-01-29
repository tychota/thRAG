import click


from rich.progress import track
from rich.console import Console
from time import sleep

console = Console()


@click.command()
@click.option("--iterations", default=5, help="Number of iterations in the demo progress bar.")
def main(iterations, debug):
    """
    Example CLI that demonstrates Rich progress bars.
    """
    # Show a Rich progress bar
    console.log("Starting a small demo loop...")
    for i in track(range(iterations), description="Processing items..."):
        sleep(0.5)  # simulate some work

    console.log("[bold green]All done![/bold green]")


if __name__ == "__main__":
    # If using as a standalone script:
    main()  # click command