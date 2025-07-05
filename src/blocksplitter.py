def markdown_to_blocks(markdown):
    valid_blocks = []
    for m in markdown.split("\n\n"):
        if not m:
            continue
        m = m.strip()
        valid_blocks.append(m)
    return valid_blocks
