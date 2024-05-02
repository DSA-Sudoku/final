from flask import flash, Blueprint, render_template, request, jsonify, session, redirect, url_for

# from app import Sudoku

main = Blueprint('main', __name__)


@main.route('/')
def home():
    username = session.get('username', 'Guest')
    return render_template('home.html', username=username)


@main.route('/easy')
def easy():
    sudoku = '...3.........8.19.71..5...44......7337...65.8..61.........154......97.....5......'
    session['sudoku'] = sudoku
    return render_template('play.html', difficulty='easy', sudoku=list(sudoku))


@main.route('/medium')
def medium():
    sudoku = '....7.....6...2.494.1..6..7.298....6...15....1.4...5..........1..65.....2...4....'
    session['sudoku'] = sudoku
    return render_template('play.html', difficulty='medium', sudoku=list(sudoku))


@main.route('/hard')
def hard():
    sudoku = '5..1.764..........413......2.....15.6.......7....754..7.4....6.86.2...1.......3.5'
    session['sudoku'] = sudoku
    return render_template('play.html', difficulty='hard', sudoku=list(sudoku))


@main.route('/play', methods=['GET', 'POST'])
def play():
    sudoku = session.get('sudoku')
    if request.method == 'POST':
        data = request.json
        x = data['x']
        y = data['y']
        num = data['num']

        # Update the Sudoku board with the inputted number at position (x, y)
        # You may use the input_num function from your Sudoku class here
        sudoku.input_num(x, y, num)

        return jsonify({'success': True})

    # Get the initial Sudoku board (you need to provide this data)
    initial_board = sudoku.return_array()
    return render_template('play.html', initial_board=initial_board)


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/instructions')
def instructions():
    return render_template('instructions.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


@main.route('/setting')
def setting():
    return render_template('setting.html')


@main.route('/leaderboard')
def leaderboard():
    return render_template('leaderboard.html')


@main.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        session['username'] = username
        flash('Logged in successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('login.html')
