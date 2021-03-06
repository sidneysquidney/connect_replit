from flask import Flask, render_template, redirect, url_for, flash

from forms import GameForm, NumberForm
from game import UIGame
from player import Human, RandomAI, MediumAI, HardAI
from grid import Piece

levels_dct = {'Easy': RandomAI, 'Medium': MediumAI, 'Hard': HardAI}
sids_game = UIGame(Human(Piece.RED), RandomAI(Piece.YELLOW))

def reset_game(level):
    global sids_game
    sids_game = UIGame(Human(Piece.RED), levels_dct[level](Piece.YELLOW))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret'

@app.route('/', methods = ['POST', 'GET'])
def setup():
    form = GameForm()
    if form.validate_on_submit():
        reset_game(form.difficulty.data)
        return redirect(url_for('game'))
    return render_template('setup.html', template_form = form)

@app.route('/game', methods = ['POST', 'GET'])
def game():
    number_form = NumberForm()
    game_over = False
    if number_form.validate_on_submit():
        if number_form.zero.data:
            move = 0
        elif number_form.one.data:
            move = 1
        elif number_form.two.data:
            move = 2
        elif number_form.three.data:
            move = 3
        elif number_form.four.data:
            move = 4
        elif number_form.five.data:
            move = 5
        elif number_form.six.data:
            move = 6
        if sids_game.valid_move(move):
            sids_game.make_move(move)
            state = sids_game.get_player_win_state()
            if state.is_ended:
                game_over = True
                if state.winner == Piece.EMPTY:
                    flash('Draw: No Winner')
                else:
                    flash('Congratulations. You are the winner!')
            else:
                sids_game.ai_move()
                state = sids_game.get_ai_win_state()
                if state.is_ended:
                    game_over = True
                    if state.winner == Piece.EMPTY:
                        flash('Draw: No Winner')
                    else:
                        flash('Unlucky. You have lost!')
        else:
            flash('Invalid move')
    return render_template('game.html', board = sids_game.move_dictionary, game_over = game_over, number_form = number_form)
