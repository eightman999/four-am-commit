import os

MESSAGE = "fix: it works now and I have no idea why, which is also how it broke, so the universe is balanced"


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(MESSAGE + "\n")


if __name__ == "__main__":
    main()
