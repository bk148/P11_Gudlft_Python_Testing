from utilis import change, points_mis_a_jour, past_competition_updated
from flask import Flask, render_template, request, redirect, flash, url_for


def create_app(config):
    app = Flask(__name__)
    app.secret_key = "something_special"
    app.config.from_object(config)

    competitions = change('competitions.json', 'competitions')
    clubs = change('clubs.json', 'clubs')

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/showSummary', methods=['POST'])
    def showSummary():
        try:
            club = [club for club in clubs if club['email'] == request.form['email']][0]
            competitions_upd = past_competition_updated(competitions)
            return render_template('welcome.html', club=club, competitions=competitions_upd)
        except IndexError:
            message = "Cette adresse mail n'existe pas"
            return render_template('index.html', message=message)

    @app.route('/book/<competition>/<club>')
    def book(competition, club):
        foundClub = [c for c in clubs if c['name'] == club][0]
        if foundClub["points"] == 0:
            flash("vous n'avez plus de point pour faire des reservations!")
            return render_template('welcome.html', club=foundClub, competitions=competitions)
        foundCompetition = [c for c in competitions if c['name'] == competition][0]
        if foundClub and foundCompetition:
            return render_template('booking.html', club=foundClub, competition=foundCompetition)
        else:
            flash("Something went wrong-please try again")
            return render_template('welcome.html', club=club, competitions=competitions)

    @app.route('/purchasePlaces', methods=['POST'])
    def purchasePlaces():
        competition = [c for c in competitions if c['name'] == request.form['competition']][0]
        club = [c for c in clubs if c['name'] == request.form['club']][0]
        placesRequired = int(request.form['places'])

        # verifier que les points sont valides
        if placesRequired < 0 or placesRequired > int(club['points']) or placesRequired > int(
                competition['numberOfPlaces']):
            flash("vous devez saisir un nombre de point valide")
            return redirect(url_for('book', club=club['name'], competition=competition['name']))
        else:
            # Mise à jour des places de competition et du club
            competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - placesRequired
            club['points'] = int(club['points']) - placesRequired

            # Les places sont competition.json et clubs.json sont correctement mise à jour
            points_mis_a_jour(
                points=str(club['points']),
                places=str(competition['numberOfPlaces']),
                id_club=clubs.index(club),
                id_comp=competitions.index(competition)
            )
            flash('Great-booking complete!')
            return render_template('welcome.html', club=club, competitions=competitions)

    # TODO: Add route for points display

    @app.route('/logout')
    def logout():
        return redirect(url_for('index'))

    return app
