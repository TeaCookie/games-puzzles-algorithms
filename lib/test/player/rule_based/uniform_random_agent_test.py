from games_puzzles_algorithms.player.rule_based.uniform_random_agent import UniformRandomAgent
from games_puzzles_algorithms.game.dex.game_state import GameState
from games_puzzles_algorithms.game.dex.game_state import COLORS
from games_puzzles_algorithms.game.dex.game_state import color_to_player
from games_puzzles_algorithms.game.dex.game_state import cell_str
from games_puzzles_algorithms.game.dex.game_state import cell_str_to_cell
import random


def test_on_empty():
    random_generator = random.Random(290134)
    state = GameState.root(5)
    patient = UniformRandomAgent(lambda: random_generator.uniform(0, 1))

    action = patient.act(state)
    action = (state.board.row(action), state.board.column(action))
    assert action == (1, 4)
    assert cell_str(action) == 'e2'
    assert action == cell_str_to_cell('e2')
    state.play(action)
    assert state.to_s(color_to_player(COLORS['white'])) == (
'''
  A  B  C  D  E
1  .  .  .  .  .  O
 2  .  .  .  .  O  O
  3  .  .  .  .  .  O
   4  .  .  .  .  .  O
    5  .  .  .  .  .  O
        @  @  @  @  @'''
    )
    assert state.to_s(color_to_player(COLORS['black'])) == (
'''
  A  B  C  D  E
1  .  .  .  .  .  O
 2  .  .  .  .  .  O
  3  .  .  .  .  .  O
   4  .  .  .  .  .  O
    5  .  .  .  .  .  O
        @  @  @  @  @'''
    )
    assert str(state) == (
'''
  A  B  C  D  E
1  .  .  .  .  .  O
 2  .  .  .  .  O  O
  3  .  .  .  .  .  O
   4  .  .  .  .  .  O
    5  .  .  .  .  .  O
        @  @  @  @  @'''
    )