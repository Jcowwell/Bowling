from Roll import Roll
from constants import FrameState, RollState
from typing import List

class Frame():
    """
        Frame Class for Bowler Program. Object for storing data for a Bowler Game's Frame.

        Data Properties:
            - rolls  : List[Roll] - List of Rolls of Frame
            - size   : int - Size of Frame
            - state  : FrameState - State of Frame
            - score  : int - Frame's score
            - addend : int - addend of Frame from SPARES & STRIKES

        When printed the object returns the following:
            - Roll {i} : Score: {score} State: {state} Symbol: {symbol}
    """
    def __init__(self, turns : int =  2, state : FrameState = FrameState.EMPTY):
        self._rolls : List[Roll] = [Roll() for _ in range(turns)]
        self._size : int = turns
        self._state : FrameState = state
        self._score : int = 0
        self._addend : int = 0
    
    @property
    def size(self) -> int:
        """
        Frame Read-Only size Property for Bowler Program. Returns number of rolls in a frame

        Data Properties:

        Returns:
            - Current number of rolls in frame (int)
        """
        return len(self._rolls)

    @property
    def state(self) -> FrameState:
        """
        Frame Get state Property for Bowler Program. Returns current FrameState of a frame. Checks a Frame's roll's RollState to report appropriate Frame status.

        Data Properties:

        Returns:
            - Current FrameState of a frame (FrameState)
        """
        if self._state == FrameState.LAST:
            return self._state
        elif self._rolls[0].state == RollState.STRIKE:
            self._state = FrameState.STRIKE
        elif self._rolls[1].state == RollState.SPARE:
            self._state = FrameState.SPARE
        elif self._rolls[0].state == RollState.OPEN:
            self._state = FrameState.OPEN
        return self._state

    @state.setter
    def state(self, state : FrameState) -> None:
        """
        Frame Set state Property for Bowler Program. Sets a Frame's FrameState.

        Data Properties:
            state: 

        Returns:
            - None
        """
        self._state = state

    @property
    def score(self) -> int:
        """
        Frame Read Only score Property for Bowler Program. Returns current Frame's score by calculating the sum of scores in a Frame's rolls and then adding the addend

        Data Properties:

        Returns:
            - Current Frame score (int)
        """
        return sum(roll.score for roll in self._rolls) + self._addend
    
    @property
    def addend(self) -> int:
        """
        Frame Get addend Property for Bowler Program. Returns the addend points of a Frame.

        Data Properties:

        Returns:
            - Current addend of a frame (int)
        """
        return self._addend
    
    @addend.setter
    def addend(self, score : int) -> None:
        """
        Frame Set score Property for Bowler Program. Sets the addend points of a Frame.

        Data Properties:
            - score : int
        Returns:
            - None
        """
        self._addend = score
    
    def __getitem__(self, index : int) -> Roll:
        """
        Frame GetItem Property for Bowler Program. Returns a Roll Object at the corresponding index.
        Will raise an IndexError if index out of range.

        Data Properties:
            index : int

        Returns:
            - A roll object at the corresponding index (int)
        """
        if not (-self._size - 1 < index < self._size):
            raise IndexError(f"Roll index out of range. This Frame has {self.size} rolls.")
        return self._rolls[index]
    
    def __setitem__(self, index : int, roll: Roll) -> None:
        """
        Frame SetItem Property for Bowler Program. Sets a Roll Object at the corresponding index.
        Will raise an IndexError if index out of range.

        Data Properties:
            index : int
            roll : Roll

        Returns:
            - None
        """
        if not (-self._size - 1 < index < self._size):
            raise IndexError(f"Roll index out of range. This Frame has {self.size} rolls.")
        score_difference : int = self._rolls[index].score - roll.score
        self._rolls[index] = roll
        self.score -= score_difference
    
    def __len__(self) -> int:
        """
        Frame len Property for Bowler Program. Returns number of Roll Objects in a frame.
        Will raise an IndexError if index out of range.

        Data Properties:

        Returns:
            - Returns number of Roll Objects in a frame (int)
        """
        return self.size
    
    def __repr__(self) -> str:
        """
        Frame repr Property for Bowler Program. Returns a string representation of a Frame.
        Will raise an IndexError if index out of range.

        Data Properties:

        Returns:
            - Returns a string representation of a Frame (str)
        """
        return f"Size: {self.size} Score: {self.score} Addend Offset: {self.addend} State: {self.state} \n" + "\n".join([f"Roll {i} : {roll}" for i, roll in enumerate(self._rolls, 1)])
