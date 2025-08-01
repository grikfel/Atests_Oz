import requests

def all_superheroes():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Ошибка \n", "Код ответа:", response.status_code)
        return []

def tallest_superhero(gender: str, work: bool):
    # Получаем список всех супергероев
    heroes_list = all_superheroes()

    # Создаем пустой список для подходящих героев
    suitable_heroes = []

    for hero in heroes_list:
        # Получаем пол героя.
        appearance = hero.get("appearance", {})
        hero_gender = appearance.get("gender", "")
        hero_gender = hero_gender.lower()

        # Получаем информацию о работе героя
        work_info = hero.get("work", {})
        occupation = work_info.get("occupation", "")
        occupation = occupation.strip()
        hero_has_work = False
        if occupation != "":
            hero_has_work = True

        # Сравниваем пол и наличие работы
        if hero_gender == gender.lower() and hero_has_work == work:
            # Получаем рост героя
            height_list = appearance.get("height", [])
            if len(height_list) > 1:
                height_str = height_list[1]  # например, "185 cm"
                height_str = height_str.replace(" cm", "")  # убираем " cm"
                try:
                    height_cm = int(height_str)
                    # Добавляем кортеж (имя, рост) в список
                    suitable_heroes.append((hero.get("name", "Без имени"), height_cm))
                except ValueError:
                    # Если не получилось преобразовать рост в число — пропускаем героя
                    continue

    # Если ни один герой не подошел, возвращаем None
    if len(suitable_heroes) == 0:
        return None

    # Ищем самого высокого героя
    tallest = suitable_heroes[0]
    for hero_data in suitable_heroes:
        name, height = hero_data
        if height > tallest[1]:
            tallest = hero_data

    # Возвращаем имя самого высокого героя
    return tallest[0]


print(tallest_superhero('Male', True))


