from flask import Flask, request, render_template
from functions import reading_candidates, reading_settings, candidate_id, search_by_name, search_by_skill

app = Flask(__name__)

@app.route('/')
def main_page():
    """
     Основная страница, выводит текст в зависимости от настройки "Online"
    """
    settings = reading_settings()
    if settings["online"] is True:
        return "Приложение работает"
    else:
        return "Приложение не работает"


@app.route('/candidate/<int:cid>/')
def candidate_data(cid):
    """
    Выводит информацию о каждом кандидате из списка по ID в заданном формате
    """
    candidate = candidate_id(cid)
    candidate_info = f"""
            <h1>{candidate["name"]}</h1>
            <p>{candidate["position"]}</p>
            <img src="{candidate["picture"]}" width=200/>
            <p>{candidate["skills"]}</p>
            """
    return candidate_info


@app.route('/list/')
def candidates_list():
    """
    Выводит список всех кандидатов
    """
    candidates = reading_candidates()
    return render_template('list.html', candidates=candidates)


@app.route('/search')
def searching_by_name_page():
    """
    Выводит список кандидатов при поиске по имени
    """
    name = request.args.get("name")
    searched_candidates = search_by_name(name)
    candidates_number = len(searched_candidates)

    search_content = f"<h2>Найдено кандидатов: {candidates_number}</h2>"

    for candidate in searched_candidates:
        search_content += f"""
            <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
            """
    return search_content


@app.route('/skill/<skill_name>')
def searching_by_skill_page(skill_name):
    """
    Выводит список кандидатов при поиске по навыку
    """
    matching_candidates= search_by_skill(skill_name)
    candidates_number = len(matching_candidates)

    search_skill_content = f"<h2>Найдено со скиллом {skill_name}: {candidates_number}</h2>"

    for candidate in matching_candidates:
        search_skill_content += f"""
                <p><a href="/candidate/{candidate["id"]}">{candidate["name"]}</a></p>
                """

    return search_skill_content

app.run()









