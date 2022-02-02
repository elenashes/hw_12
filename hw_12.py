from flask import Flask, request
from functions import reading_candidates, reading_settings, candidate_id, search_by_name, search_by_skill

app = Flask(__name__)

@app.route('/')
def main_page():
    settings = reading_settings()
    if settings["online"] is True:
        return "Приложение работает"
    else:
        return "Приложение не работает"


@app.route('/candidate/<int:сid>/')
def candidate_data(сid):
    candidate = candidate_id(сid)
    candidate_info = f"""
            <h1>{candidate["name"]}</h1>
            <p>{candidate["position"]}</p>
            <img src="{candidate["picture"]}" width=200/>
            <p>{candidate["skills"]}</p>
            """
    return candidate_info


@app.route('/list')

def candidates_list():
    candidates = reading_candidates()
    list_content = '<h1>Все кандидаты</h1>'
    for candidate in candidates:
        list_content += f"""
            <p><a href ="/candidate{candidate["id"]}">{candidate["name"]}</a></p>
            """
        return list_content

@app.route('/search')

def searching_by_name_page():
    name = request.args.get("name")
    candidates = search_by_name(name)
    candidates_number = len(candidates)

    search_content = f"<h2>Найдено кандидатов: {candidates_number}</h2>"

    for candidate in candidates:
        search_content += f"""
            <p><a href="/candidate/{candidate["id"]}>{candidate["name"]}</a></p>
            """
    return search_content


@app.route('/skill/<skill_name>')

def searching_by_skill_page(skill_name):
    candidates = search_by_skill(skill_name)
    candidates_number = len(candidates)

    search_content = f"<h2>Найдено со скиллом {skill_name}: {candidates_number}</h2>"

    for candidate in candidates:
        search_content += f"""
                <p><a href="/candidate/{candidate["id"]}>{candidate["name"]}</a></p>
                """

    return search_content

app.run()









