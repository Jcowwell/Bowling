from constants import RollState, Symbols

class Roll():
    """
        Roll Class for Bowler Program. Object for storing data for a Bowler Game Frame's Roll.

        Data Properties:
            - score : int
            - state : RollState
            - symbol : str

        When printed the object returns the following:
            - Score: {score} State: {state} Symbol: {symbol}
    """
    def __init__(self, score : int = 0, state : RollState = RollState.EMPTY):
        self._score : int = score
        self._state : RollState = state
        self._symbol : str = Symbols[self._state]
    
    @property    
    def score(self) -> int:
        """
        Roll Get score Property for Bowler Program. Returns current score of a Roll.

        Data Properties:

        Returns:
            - Current score of a Roll (int)
        """
        return self._score

    @score.setter
    def score(self, score : int) -> None:
        """
        Roll Set score Property for Bowler Program. Will automatically set a Roll's state to Open or Stike depending on score.

        Data Properties:
            score : int

        Returns:
            - None
        """
        if score == 0:
            self.state = RollState.OPEN
        elif score == 10:
            self.state = RollState.STRIKE
        self._score = score

    @property
    def state(self) -> RollState:
        """
        Roll Get state Property for Bowler Program. Returns current state of a Roll.

        Data Properties:

        Returns:
            - Current state of a Roll (RollState)
        """
        return self._state

    @state.setter
    def state(self, state : RollState) -> None:
        """
        Roll Get state Property for Bowler Program. Sets current state of a Roll.

        Data Properties:
            state : RollState

        Returns:
            - None
        """
        self._state = state
    
    @property
    def symbol(self) -> str:
        """
        Roll Read Only symbol Property for Bowler Program. Returns a string representation of the current score of a Roll.

        Data Properties:

        Returns:
            - A string representation of the current score of a Roll (str)
        """
        if self._state == RollState.OPEN:
            return Symbols[self.score]
        else:
            return Symbols[self.state]
    
    def __repr__(self) -> str:
        """
        Roll repr Property for Bowler Program. Returns a string representation of a Roll.

        Data Properties:

        Returns:
            - Returns a string representation of a Roll (str)
        """
        return f"Score: {self.score} State: {self.state} Symbol: {self.symbol}"
