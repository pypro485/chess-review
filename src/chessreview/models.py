from dataclasses import dataclass

@dataclass
class MoveAnalysis:
    ply: int
    san: str
    mover: str
    fen_after: str
    eval_before: int
    eval_after: int
    drop: float
    best_move_san: str
    label: str



@dataclass
class GameReview:
    headers: dict[str, str]
    moves: list[MoveAnalysis]


if __name__ == "__main__":
    analysis = MoveAnalysis(
        ply=6,
        san="Nxe4",
        mover="Black",
        fen_after="rnbqkb1r/pppp1ppp/8/4p3/4n3/2N2N2/PPPP1PPP/R1BQKB1R w KQkq - 0 4",
        eval_before=-24,
        eval_after=-248,
        drop=19.2,
        best_move_san="Bb4",
        label="Mistake",
    )
    print(analysis)
    print(analysis.drop)
    print(analysis.label)