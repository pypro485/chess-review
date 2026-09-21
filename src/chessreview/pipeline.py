import os
from collections import Counter
import chess.pgn
import chess.engine
from dotenv import load_dotenv
from src.chessreview.scoring import win_pct
from src.chessreview.classifier import classify, MISS_MIN, MISS_TRIGGER
from src.chessreview.models import MoveAnalysis
from src.chessreview.openings import load_openings, lookup
load_dotenv()
STOCKFISH_PATH = os.getenv("STOCKFISH_PATH")
def review_game(game, depth=12):
    board = game.board()

    with chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH) as engine:
        game_token = object()
        engine.configure({"Threads": 1, "Hash": 512})
        prev = engine.analyse(board, chess.engine.Limit(depth=depth), game=game_token)
        openings = load_openings()
        prev_drop = 0
        is_book = True
        results = []
        for move in game.mainline_moves():
            best_move = prev["pv"][0]
            san = board.san(move)
            mover = board.turn
            best_move_san = board.san(best_move)
            board.push(move)
            ply = board.ply()
            book_name = lookup(board, openings)
            info = engine.analyse(board, chess.engine.Limit(depth=depth), game=game_token)
            score = info["score"].pov(mover)
            before_score = prev["score"].pov(mover)
            before_score_int = before_score.score(mate_score=10000)
            score_int = score.score(mate_score=10000)
            if mover == chess.WHITE:
                turn_str = "White"
            else:
                turn_str = "Black"
            if book_name is None:
                is_book = False
            drop = win_pct(before_score_int) - win_pct(score_int)
            is_miss = prev_drop >= MISS_TRIGGER and drop > MISS_MIN
            move_classify = classify(drop, move == best_move, is_book, is_miss)
            move_obj = MoveAnalysis(
                ply=ply,
                san=san,
                mover=turn_str,
                fen_after=board.fen(),
                eval_before=before_score_int,
                eval_after=score_int,
                drop=drop,
                best_move_san=best_move_san,
                label=move_classify
            )
            results.append(move_obj)
            prev = info
            prev_drop = drop
        return results