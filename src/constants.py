
from typing import Dict, Union
from enum import Enum, auto

class RollState(Enum):
    EMPTY = auto()
    OPEN = auto()
    SPARE = auto()
    STRIKE = auto()
    STRIKED = auto()
    FOUL = auto()
    SPLIT = auto()

    def __str__(self):
        return str(self.name)

class FrameState(Enum):
    EMPTY = auto() # no scores
    OPEN = auto() # no strikes or spares
    SPARE = auto() # spare occured
    STRIKE = auto() # striked occured
    LAST = auto() # last frame in the game

    def __str__(self):
        return str(self.name)

class GameState(Enum):
    FIRST_ROLL = auto()
    SECOND_ROLL = auto()
    SPARE_A_ROLL_AGO = auto()
    STRIKE_A_ROLL_AGO = auto()
    CONSECTUIVE_STRIKES = auto()
    STRIKE_TWO_ROLLS_AGO = auto()
    BONUS = auto()
    GAME_END = auto()

    def __str__(self):
        return str(self.name)
    
class RollStageEnum(Enum):
    FIRST_ROLL = 1
    SECOND_ROLL = 2
    THIRD_ROLL = 3
    GAME_OVER = -1

    def __str__(self):
        if self.value == 1:
            return 'First Roll'
        elif self.value == 2:
            return 'Second Roll'
        elif self.value == 3:
            return 'Third Roll'
        elif self.value == -1:
            return 'Game Over'
        return str(self.value)

RollStage : Dict[GameState, RollStageEnum] = {
    GameState.FIRST_ROLL : RollStageEnum.FIRST_ROLL,
    GameState.SECOND_ROLL : RollStageEnum.SECOND_ROLL,
    GameState.SPARE_A_ROLL_AGO : RollStageEnum.FIRST_ROLL,
    GameState.STRIKE_A_ROLL_AGO : RollStageEnum.FIRST_ROLL,
    GameState.CONSECTUIVE_STRIKES : RollStageEnum.FIRST_ROLL,
    GameState.STRIKE_TWO_ROLLS_AGO : RollStageEnum.SECOND_ROLL,
    GameState.BONUS : RollStageEnum.THIRD_ROLL,
    GameState.GAME_END : RollStageEnum.GAME_OVER,
}

Symbols : Dict[Union[RollState, int], str] = {
    RollState.EMPTY : '',
    RollState.SPARE : '/',
    RollState.STRIKE : 'X',
    RollState.STRIKED : '',
    0 : '-',
    1 : '1',
    2 : '2',
    3 : '3',
    4 : '4',
    5 : '5',
    6 : '6',
    7 : '7',
    8 : '8',
    9 : '9',
    10 : 'X'
}