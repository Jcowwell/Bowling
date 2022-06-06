from Frame import Frame
from constants import GameState, RollStage, FrameState, RollState
from typing import List

class ScoreKeeper():
    """
        ScoreKeeper Class for Bowler Program. Object for storing scoring data and game state for a Bowler Game program.

        Data Properties:
            - frame : int
            - score : int
            - pins : int
            - rounds : int
            - movesRemaining : int
            - roll : None
            - showScoreboard : None
    """

    def __init__(self, rounds: int = 10, verbose : bool = False):
        self._frames : List[Frame] = [Frame() for _ in range(rounds - 1)] + [Frame(turns=3, state=FrameState.LAST)]
        self._frame : int = 0 # 0-frames
        self._state : GameState = GameState.FIRST_ROLL
        self._score : int = 0 
        self._pins : int = 10
        self._rounds : int = rounds
        self._verbose : bool = verbose
    
    @property
    def frame(self) -> int:
        """
        ScoreKeeper Read-Only frame Property for Bowler Program. Returns current frame of the Game.

        Data Properties:

        Returns:
            - Current frame of the game (int)
        """
        return self._frame
    
    @property
    def score(self) -> int:
        """
        ScoreKeeper Read-Only score Property for Bowler Program. Returns current score of a Game.

        Data Properties:

        Returns:
            - Current score of the game (int)
        """
        return self._score
    
    @property
    def pins(self) -> int:
        """
        ScoreKeeper Read-Only pin Property for Bowler Program. Returns current pins of a Game.

        Data Properties:

        Returns:
            - Current number of pins standing (int)
        """
        return self._pins

    @property
    def rounds(self) -> int:
        """
        ScoreKeeper Read-Only round Property for Bowler Program. Returns current round of a Game.

        Data Properties:

        Returns:
            - Current round (int)
        """
        return self._rounds
    
    def movesRemaining(self) -> int:
        """
        ScoreKeeper movesRemaining Method for Bowler Program. Returns number of moves left in a Game.

        Data Properties:

        Returns:
            - Number of moves left in the game (int)
        """
        if self._state == GameState.GAME_END:
            return 0
        current_roll: int = RollStage[self._state].value
        if self.rounds - 1 == self.frame: # we are on the last frame:
            if current_roll == 2 and self._frames[self.frame].state == FrameState.STRIKE:
                return 2
            if current_roll == 3:
                return 1
            return 2 - (current_roll - 1)

        # get the number of frames left
        remaining_frames: int = self.rounds - self.frame - 1
        return (remaining_frames * 2 + 3) - (RollStage[self._state].value - 1)

    def roll(self, pins) -> None:
        """
        ScoreKeeper roll method for Bowler Program. Handles the game stage mechanics of a game and allocates points.

        Data Properties:
            - pins : int - Number of pins that are knocked

        Returns:
            - None
            - If ScoreKeeper's verbose attribute if enabled roll will print the game's progress after each turn.
        """
        # validaiton
        if pins < 0 or pins > self._pins:
            raise Exception(f"Roll Exceeds # of Available Pins. \n Roll: {pins} , Available Pins: {self._pins}")

        if self._state == GameState.GAME_END:
            print("Sorry! The Game is Over. Would you Like to Restart?")
            keep_playing: str = input("Y/N?")
            if keep_playing == "Y":
                self.__init__()
            elif keep_playing == "N":
                print("Goodbye!")
                return
            else:
                print("Sorry! Please enter Y or N")
                return

        self._score += pins # running total

        if self._state == GameState.FIRST_ROLL:

            self._first_roll(self._frame, GameState.STRIKE_A_ROLL_AGO, GameState.SECOND_ROLL, pins)

        elif self._state == GameState.SECOND_ROLL:
        
            self._second_roll(self._frame, GameState.SPARE_A_ROLL_AGO, GameState.FIRST_ROLL, pins)
            
        elif self._state == GameState.SPARE_A_ROLL_AGO: # can only be true during first roll 
            
            self._addend(self._frame - 1, pins)

            self._first_roll(self._frame, GameState.STRIKE_A_ROLL_AGO, GameState.SECOND_ROLL, pins)

        elif self._state == GameState.STRIKE_A_ROLL_AGO: # can only be true during first roll
            
            self._addend(self._frame - 1, pins)

            self._first_roll(self._frame, GameState.CONSECTUIVE_STRIKES, GameState.STRIKE_TWO_ROLLS_AGO, pins)

        elif self._state == GameState.CONSECTUIVE_STRIKES: # can only be true during first roll

            self._addend(self._frame - 2, pins)
            self._addend(self._frame - 1, pins)

            self._first_roll(self._frame, GameState.CONSECTUIVE_STRIKES, GameState.STRIKE_TWO_ROLLS_AGO, pins)

        elif self._state == GameState.STRIKE_TWO_ROLLS_AGO: # can only be true during second roll

            self._addend(self._frame - 1, pins)

            self._second_roll(self._frame, GameState.SPARE_A_ROLL_AGO, GameState.FIRST_ROLL, pins)
        
        # can only occur in the tenth frame and if first roll is a STRIKE or second roll is a SPARE
        elif self._state == GameState.BONUS:
            self._frames[self._frame][2].score = pins
            self._frames[self._frame][2].state = RollState.STRIKE if pins == 10 else RollState.OPEN
            self._state = GameState.GAME_END
            if self._verbose:
                self.show_scoreboard()
        
        if self._verbose:
            self.show_scoreboard()

    def _first_roll(self, frame: int, game_state: GameState, alternative_game_state: GameState, pins: int) -> None:
        """
        ScoreKeeper private void First Roll method for Bowler Program. Handles the first roll logic and sets the gamestate acccordingly.

        Data Properties:
            frame : int
            game_state : GameState
            alternative_game_state: GameState
            pins: int

        Returns:
            - None
            - Will act differently when the game is in the last Frame
        """

        self._frames[frame][0].score += pins
        state: FrameState = self._frames[frame].state

        if pins == 10 and state != FrameState.LAST: # STRIKE
            self._state = game_state # set game state
            self._frames[frame][0].state = RollState.STRIKE # set frame roll 1 state
            self._frames[frame][1].state = RollState.STRIKED # set frame roll 2 state
            self._frame = frame + 1 # move to next frame
        elif pins == 10 and state == FrameState.LAST:
            self._frames[frame][0].state = RollState.STRIKE
            self._state = alternative_game_state
        else: # OPEN
            self._frames[frame][0].state = RollState.OPEN
            self._state = alternative_game_state
            self._pins -= pins
    
    def _second_roll(self, frame: int, game_state: GameState, alternative_game_state: GameState, pins: int) -> None:
        """
        ScoreKeeper private void Second Roll method for Bowler Program. Handles the second roll logic and sets the gamestate acccordingly. 
        Will reset the pins 

        Data Properties:
            frame : int
            game_state : GameState
            alternative_game_state: GameState
            pins: int

        Returns:
            - None
            - Will act differently when the game is in the last Frame
        """

        self._frames[frame][1].score += pins
        state: FrameState = self._frames[frame].state

        if self._frames[frame].score == 10 and state != FrameState.LAST: # SPARE
            self._state = game_state # set game state
            self._frames[frame][1].state = RollState.SPARE # set frame roll 1 state
        elif state == FrameState.LAST and self._frames[frame][1].score == 10: # STRIKE
            self._state = GameState.BONUS
            self._frames[frame][1].state = RollState.STRIKE if self._frames[frame][0].state == RollState.STRIKE else RollState.SPARE
            self._reset_pins()
            return
        elif state == FrameState.LAST and self._frames[frame][1].score < 10: # not a STRIKE but can be a SPARE
            self._state = GameState.BONUS if self._frames[frame].score >= 10 else GameState.GAME_END
            self._frames[frame][1].state = RollState.OPEN if self._frames[frame].score < 10 else RollState.SPARE
            self._reset_pins()
            return
        else: # OPEN
            self._state = alternative_game_state
            self._frames[frame][1].state = RollState.OPEN # set frame state
        
        self._reset_pins()
        self._frame = frame + 1 # move to next frame

    def _addend(self, frame: int , pins: int) -> None:
        """
        ScoreKeeper private void Addend method for Bowler Program. Handles point allocation for previous frames that were strikes or spares.

        Data Properties:
            frame : int
            pins: int

        Returns:
            - None
        """
        self._frames[frame].addend += pins
        self._score += pins
    
    def _reset_pins(self) -> None:
        """
        ScoreKeeper private void Reset Pins method for Bowler Program. Handles resetting the pin variable. 

        Data Properties:

        Returns:
            - None
        """
        self._pins = 10
    
    def show_scoreboard(self):
        """
        ScoreKeeper public void Show Scoreboard method for Bowler Program. Prints a custom grid view of a game's progress including current round, frame, score, remaining pins, and moves.

        Data Properties:

        Returns:
            - None
        
        # Adopted from: https://github.com/BnkColon/bowling-scoreboard/blob/b7711251eaf43e4c1833d69467bec53c54af2ecb/bowling-scoreboard.py#L114 
        """
        

        start = "\033[1m"
        end = "\033[0;0m"

        # Print the table
        print("")
        print(start+"Bowling Game"+end)
        print("-------------------------------------------")
        print("Current Frame : {:<4} Current Pins : {:<4}".format(self.frame + 1, self.pins)) 
        print("Current Score : {:<4} Current Roll : {:<4}".format(self.score, RollStage[self._state]))
        print("Moves Remaining : {:<4} ".format(self.movesRemaining()))
        print("-------------------------------------------")
        print("{:<8} {:<8} {:<8} {:<8} {:<8}".format('FR','R1', 'R2', 'R3', 'Score'))
        print("-------------------------------------------")
        cumulative_score : int = 0
        for i in range(self.rounds - 1):
            frame : Frame = self._frames[i]
            score = str(frame.score + cumulative_score) if frame[1].state != RollState.EMPTY else str(frame[0].score + cumulative_score) if frame[0].state != RollState.EMPTY else "" 
            print("{:<8} {:<8} {:<8} {:<8} {:<8}".format(i + 1, frame[0].symbol, frame[1].symbol, "", score))
            print("-------------------------------------------")
            cumulative_score += frame.score
        frame : Frame = self._frames[self.rounds - 1]
        score = str(frame.score + cumulative_score) if frame[1].state != RollState.EMPTY else str(frame[0].score + cumulative_score) if frame[0].state != RollState.EMPTY else "" 
        print("{:<8} {:<8} {:<8} {:<8} {:<8}".format(self.rounds, frame[0].symbol, frame[1].symbol, frame[2].symbol, score))
        print("-------------------------------------------")
        if (self._state == GameState.GAME_END):
            print("{:<8} {:<8} {:<8} {:<8} {:<8}".format('Total','', '', '', self.score))
            print("-------------------------------------------")
