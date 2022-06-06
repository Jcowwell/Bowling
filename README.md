# Bowling
Python-Based Bowling ScoreKeeper Program.

A couple of days ago, I interviewed a company. It went horrible. Don't get me wrong; it wasn't the company's fault. They were kind, reassuring, and patient.
It was **me**. I was a nervous blubbering mess who wasted 20 minutes on *syntax* and kept flipflopping my solution every 5 seconds. I wasn't even able to show a solution to a relatively easy problem by the end.
After the interview, I immediately went to sleep. I was crushed. I incinerated any chance I had with the company, and most importantly, my pride as a programmer was wounded. 
Imposter Syndrome threatened to take hold of me, and I was deliberating on going back to Grad School as I was surely not ready.
Later that night, I spawned up a new VSCode window and Jupyter Notebook and went to work. I couldn't face myself if I didn't solve this rudimentary problem.
This program is the result. It's not perfect, and I still have to write up some test cases to see if it truly works, but it's enough where I can say, "I can at least code."
While I'm still bummed about my embarrassingly display, I am grateful for the opportunity. 

This is a Bowling ScoreKeeper Program. it utilizes 3 classes: *Roll*, *Frame*, and *ScoreKeeper*.
  - **Roll** is a class designed to keep track of the status and score of a roll round.
  - **Frame** is a class designed to keep track of the total score of a group of Rolls and addend points in the event of a Stirke or Spare. 
    - A Frame object also keeps track of a Frame Status (i.e Strike, Spare, Last Frame) 
  - **ScoreKeeper** is a class designed to keep track of a game's score, state, pins, calculate a roll input, and report a game's status via a custom print scoreboard.
