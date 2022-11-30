# Connect4
This is a Connect4 game where the user can play (and lose/draw) against the computer.  I have three goals behind this project:
1. Learn the fundamentals of Python in terms of syntax, OOP, algorithms, data structures, libraries, and more
2. Explore AI by implementing the [minimax algorithm](https://en.wikipedia.org/wiki/Minimax) with [alpha-beta pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning) to decide the computer's moves
3. Adopt best practices in Python programming ([Official style guide](https://peps.python.org/pep-0008/#whitespace-in-expressions-and-statements), [Google style guide](https://google.github.io/styleguide/pyguide.html), [Hitchhiker’s Guide](https://docs.python-guide.org/))

## How to run the game?
1. Ensure Python 3 and Pygame are installed in your terminal
2. Enter the following command in your terminal: `python3 Connect4.py`
3. After the window appears, you can start playing by clicking at the column you wish to place your piece in

Note: For the first few moves, the AI takes around 30-40s. Also, for some computers, the AI's response might be too slow (60+). To speed it up, you may lower the `DEPTH` in `Constants.py` (say, from 6 to 5 or 4). But beware, this will hurt the AI's ability to make good moves.

## Possible future improvements
### Graphics
This is the elephant in the room. The coin pieces are pixilated and appear too suddenly, while there's no information on the window. I neglected graphics because my focus was the algorithm for the AI's moves. I will look into improving the graphics in later commits.

### Scoring
During this project, I realized that minimax is only as good as the scores fed into it. The scores here are assessments made of different game states, where positive/negative scores indicate the AI/user is winning; the greater the absolute value, the more one-sided the game state is. 

My current approach only analyzes continuous links, where the longer the link of same colors, the greater the score. For example, two continuous pieces will get a lower score than three continuous pieces. This makes sense and is a widely used approach in analyzing Connect4 game states. 

The problem is that this approach doesn't account for discontinuous pieces that have the potential to produce long, continuous links. For instance, two continuous pieces will have the same score as another set of two pieces separated by one other piece (i.e. score[_*\*_] = score[_**\_*_]). Obviously, one has more potential than the other. Currently, this isn't an issue because even single pieces with empty spaces adjecent to it are given a score. But it could be a problem if `DEPTH` is lowered. A future commit would adjust the scoring algorithm in `Scoring.py` to account for discontinuous links.

### Coding style
I haven't fully adhered to my third goal: adopting best practices in python programming. While I have modularized my code quite a bit, there are still repetitions and redundancies here and there. Furthermore, I haven't implemented any of the aforementioned style guides in the interest of time. This is something I will address in a future commit.
