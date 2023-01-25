from models.Game import Game
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
jogo = Game()
title = "FutQuero v1"


@app.route('/list')
def list():
    return render_template('list.html',
                           titulo=title,
                           players=jogo.players,
                           error=jogo.error,
                           sucess=jogo.sucess)


@app.route('/', methods=['GET', 'POST'])
def page_match():
    print(jogo.players)
    print(jogo.avaliables)
    return render_template('match.html',
                           titulo=title,
                           team1=jogo.team1,
                           team2=jogo.team2,
                           resultado=jogo.resultado,
                           avaliables=jogo.avaliables,
                           minutes=jogo.time_min,
                           seconds=jogo.time_sec)


@app.route('/config')
def config():
    return render_template('config.html')


@app.route('/reset', methods=['POST'])
def reset():
    jogo.reset()
    return redirect('/')

# Actions Lista


@app.route('/add', methods=['POST'])
def add_player():
    if request.method == "POST":
        player_name = request.form.get("player")
        jogo.add_player(player_name)
        if player_name in jogo.avaliables:
            jogo.error = "Player already exists."
        else:
            jogo.avaliables.append(player_name)

    return redirect('/list')


@app.route('/remove/<name>', methods=['POST'])
def remove_player(name):
    jogo.remove_player(name)
    jogo.change_player(name)
    if name in jogo.avaliables:
        jogo.avaliables.remove(name)
    else:
        pass
    print(name)
    return redirect('/list')


@app.route('/set_avaliable', methods=['POST'])
def set_avaliable():
    lista = []
    if request.method == 'POST':
        lista = request.form.getlist("avaliables")

    for name in lista:
        if any(player["name"].capitalize() == name.capitalize() for player in jogo.players):
            return "checado"
        else:
            jogo.change_player(name)
            print(name)

    return redirect('/list')


# Action Match

@app.route('/set_match', methods=['POST'])
def set_match():
    jogo.match()
    return redirect('/')


@app.route('/end_match', methods=['POST'])
def end_match():
    jogo.winner()
    return redirect('/')


@app.route('/score/<team_scored>', methods=['POST'])
def score(team_scored):
    jogo.score(team_scored)
    return redirect('/')

# Action Tempo


@app.route('/start_time', methods=['POST'])
def play():
    jogo.play()
    print("funfou")
    return redirect('/')


@app.route('/pause_time/{{ paused }}', methods=['POST'])
def pause(paused):
    jogo.pause()
    has_paused = paused
    return redirect('/')


@app.route('/reset_time', methods=['POST'])
def reset_timer():
    jogo.reset_timer()
    return redirect('/')


app.run(debug=True)
