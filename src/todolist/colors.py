"""Color support for terminal output."""

import os
import sys
from typing import Optional


class Colors:
    """ANSI color codes for terminal output."""

    # Basic colors
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    UNDERLINE = "\033[4m"

    # Text colors
    BLACK = "\033[30m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"

    # Bright text colors
    BRIGHT_BLACK = "\033[90m"
    BRIGHT_RED = "\033[91m"
    BRIGHT_GREEN = "\033[92m"
    BRIGHT_YELLOW = "\033[93m"
    BRIGHT_BLUE = "\033[94m"
    BRIGHT_MAGENTA = "\033[95m"
    BRIGHT_CYAN = "\033[96m"
    BRIGHT_WHITE = "\033[97m"

    # Background colors
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"


def supports_color() -> bool:
    """Check if the terminal supports color output.

    Returns:
        True if color is supported, False otherwise
    """
    # Check if running in CI or if color is explicitly disabled
    if os.getenv("NO_COLOR") or os.getenv("CI"):
        return False

    # Check if stdout is a TTY
    if not hasattr(sys.stdout, "isatty"):
        return False

    if not sys.stdout.isatty():
        return False

    # Windows support
    if sys.platform == "win32":
        # Windows 10+ supports ANSI colors
        return True

    return True


def colorize(text: str, color: str, bold: bool = False) -> str:
    """Apply color to text if color is supported.

    Args:
        text: Text to colorize
        color: Color code from Colors class
        bold: Whether to make text bold

    Returns:
        Colored text if supported, otherwise plain text
    """
    if not supports_color():
        return text

    style = Colors.BOLD if bold else ""
    return f"{style}{color}{text}{Colors.RESET}"


def color_priority(priority: str) -> str:
    """Get colored priority indicator.

    Args:
        priority: Priority level (high, medium, low)

    Returns:
        Colored priority string
    """
    priority_upper = priority.upper()

    if priority.lower() == "high":
        return colorize(f"!!! {priority_upper}", Colors.RED, bold=True)
    elif priority.lower() == "medium":
        return colorize(f"!!  {priority_upper}", Colors.YELLOW, bold=True)
    else:  # low
        return colorize(f"!   {priority_upper}", Colors.BLUE)


def color_status(status: str) -> str:
    """Get colored status indicator.

    Args:
        status: Task status (pending or completed)

    Returns:
        Colored status icon
    """
    if status == "completed":
        return colorize("✓", Colors.GREEN, bold=True)
    else:  # pending
        return colorize("○", Colors.YELLOW)


def success(text: str) -> str:
    """Format success message.

    Args:
        text: Message text

    Returns:
        Colored success message
    """
    return colorize(text, Colors.GREEN, bold=True)


def error(text: str) -> str:
    """Format error message.

    Args:
        text: Error message text

    Returns:
        Colored error message
    """
    return colorize(text, Colors.RED, bold=True)


def warning(text: str) -> str:
    """Format warning message.

    Args:
        text: Warning message text

    Returns:
        Colored warning message
    """
    return colorize(text, Colors.YELLOW, bold=True)


def info(text: str) -> str:
    """Format info message.

    Args:
        text: Info message text

    Returns:
        Colored info message
    """
    return colorize(text, Colors.CYAN)


def dim(text: str) -> str:
    """Format dimmed text.

    Args:
        text: Text to dim

    Returns:
        Dimmed text
    """
    if not supports_color():
        return text
    return f"{Colors.DIM}{text}{Colors.RESET}"
