import os

# One Line, Big Laugh: the setup promises a soothing sound, then the
# punchline reframes "relaxing" as the last thing a bank statement is.
# The twist lands in the final word, so the whole line is the joke.
ENTRY_LINE = "I asked my smart speaker to play something relaxing. It played my bank statement as an audiobook."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        # One line only, no trailing newline: the file IS the joke.
        f.write(ENTRY_LINE)


if __name__ == "__main__":
    main()
