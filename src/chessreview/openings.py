import csv
import io
from pathlib import Path

import chess
import chess.pgn

OPENINGS_DIR = Path(__file__).resolve().parents[2] / "data" / "openings"


def load_openings():
    """Read all five ECO files and return {position: opening name}."""
    openings = {}
    for letter in "abcde":
        with open(OPENINGS_DIR / f"{letter}.tsv", newline="") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                game = chess.pgn.read_game(io.StringIO(row["pgn"]))
                board = game.end().board()
                openings[board.epd()] = row["name"]
    return openings


def lookup(board, openings):
    """Return the opening name for this position, or None if it's not book."""
    return openings.get(board.epd())


if __name__ == "__main__":
    openings = load_openings()
    print(len(openings))

    board = chess.Board()
    board.push_san("e4")
    board.push_san("e5")
    print(lookup(board, openings))