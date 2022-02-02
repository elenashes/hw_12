import json

def reading_candidates():
    with open('candidates.json', 'r', encoding="utf-8") as file:
        candidate_data_json = json.load(file)
    return candidate_data_json

def reading_settings():
    with open('settings.json', 'r', encoding="utf-8") as file:
        settings = json.load(file)
    return settings

def candidate_id(сid):
    candidates = reading_candidates()
    for candidate in candidates:
        if int(candidate["id"]) == int(сid):
            return candidate

def search_by_name(name):
    settings = reading_settings()
    case_sensitive = settings["case-sensitive"]
    candidates = reading_candidates()
    matching_candidates = []

    for candidate in candidates:
        if name in candidate["name"]:
            matching_candidates.append(candidate)
            continue

        if not case_sensitive:
            if name.lower() in candidate["name"].lower():
                matching_candidates.append(candidate)

    return matching_candidates


def search_by_skill(skill_name):
    settings = reading_settings()
    limit = settings["limit"]

    candidates = reading_candidates()
    matching_candidates = []

    skill_name = skill_name.lower()

    for candidate in candidates:
        if skill_name in candidate["skills"]:
            matching_candidates.append(candidate)

    return matching_candidates[:limit]

