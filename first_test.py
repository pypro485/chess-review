import chess.pgn
from collections import Counter
from src.chessreview.pipeline import review_game
from src.chessreview.models import GameReview
from src.chessreview.storage import save_review, load_review
with open("data/sample_games/game1.pgn") as f:
    game = chess.pgn.read_game(f)

results = review_game(game, depth=18)
counts = {"White": Counter(), "Black": Counter()}
for m in results:
    print(f"{m.san:8} {m.eval_after:+} {m.mover} Before:{m.eval_before:+} Drop:{m.drop:.1f} Type: {m.label}")
    counts[m.mover][m.label] += 1
review = GameReview(dict(game.headers), results)
save_review(review, 'data/reviews/game1.json')
loaded = load_review("data/reviews/game1.json")
print(loaded == review)