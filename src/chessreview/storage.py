import json
from dataclasses import asdict
from src.chessreview.models import MoveAnalysis, GameReview
def save_review(review, path):
    with open(path, 'w') as f:
        json.dump(asdict(review), f, indent=2)

def load_review(path):
    moves = []
    with open(path) as f:
        data = json.load(f)
        for move in data["moves"]:
            moves.append(MoveAnalysis(**move))

    return GameReview(headers=data["headers"], moves=moves)
        
