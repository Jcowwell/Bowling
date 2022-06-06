from typing import List, Optional
from ScoreKeeper import ScoreKeeper

def moves() -> List[List[Optional[int]]]:
    # FIXME: add logic to random generate bowling gmae
    return [
        [9,1],
        [0,10],
        [10,None],
        [10,None],
        [6,2],
        [7,3],
        [8,2],
        [10,None],
        [9,0],
        [10,10,7]
    ]

def play(moves : List[List[Optional[int]]], scoreKeeper : ScoreKeeper = ScoreKeeper()):
    for i in range(len(moves) - 1):
        first_roll, second_roll = moves[i]
        scoreKeeper.roll(first_roll)
        if second_roll is not None:
            scoreKeeper.roll(second_roll)
    first_roll, second_roll, third_roll = moves[len(moves) - 1]
    scoreKeeper.roll(first_roll)
    scoreKeeper.roll(second_roll)
    if third_roll is not None:
        scoreKeeper.roll(third_roll)


def main() -> None:
    scoreKeeper : ScoreKeeper = ScoreKeeper(verbose=True)
    play(moves=moves(), scoreKeeper=scoreKeeper)

if __name__ == '__main__':
    main()
