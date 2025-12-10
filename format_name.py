def make_pretty_name(raw_name: str) -> str:
    """
    Takes a raw name string, trims whitespace, converts to title case,
    and decorates it with emojis for display.
    """
    if not isinstance(raw_name, str):
        raise TypeError("Name must be a string")

    cleaned = raw_name.strip().title()
    return f"🌸 Hello {cleaned}! 🌸"
