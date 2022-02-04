import json

def reading_candidates():
    """
    функция для чтения списка кандидатов из json-файла
    """
    with open('candidates.json', 'r', encoding="utf-8") as file:
        candidate_data_json = json.load(file)
    return candidate_data_json

def reading_settings():
    """
    Функция для считывания настроек из json-файла
    """
    with open('settings.json', 'r', encoding="utf-8") as file:
        settings = json.load(file)
    return settings

def candidate_id(uid):
    """
    Функция для составления профиля кандидата по id
    """
    candidates = reading_candidates()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate

def search_by_name(name):
    """
    Функция для поиска кандидатов по имени, возвращает список
    """
    settings = reading_settings()
    case_sensitive = settings["case-sensitive"]
    candidates = reading_candidates()
    searched_candidates = []

    for candidate in candidates:
        if name in candidate["name"]:
            searched_candidates.append(candidate)
            continue

        if not case_sensitive:
            if name.lower() in candidate["name"].lower():
                searched_candidates.append(candidate)

    return searched_candidates


def search_by_skill(skill_name):
    """
    Функция для поиска кандидатов по навыкам, возвращает список кандидатов
    """
    settings = reading_settings()
    limit = settings["limit"]

    candidates = reading_candidates()
    matching_candidates = []

    skill_name = skill_name.lower()

    for candidate in candidates:
        if skill_name in candidate["skills"]:
            matching_candidates.append(candidate)

    return matching_candidates[:limit]

