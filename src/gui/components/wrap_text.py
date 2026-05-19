def WrapText(text, max_len=18):
    text = text.replace('>', ' > ')
    words = text.split()
    lines, cur = [], ""
    # Символ ">" переносить на новий рядок(він невидимий)
    # The symbol ">" moves to a new line (it is invisible).
    for w in words:
        if w == '>':
            if cur:
                lines.append(cur)
            cur = ""
            continue

        if len(cur) + len(w) + 1 <= max_len:
            cur += (" " if cur else "") + w
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)

    return "\n".join(lines)