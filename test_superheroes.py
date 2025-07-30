import pytest
from main import tallest_superhero

# Создаем подменную функцию с нужными данными для проверки
def change_superheroes():
    return [
        {
            "name": "Hero1",
            "appearance": {"gender": "Male", "height": ["5", "180 cm"]},
            "work": {"occupation": "Engineer"}
        },
        {
            "name": "Hero2",
            "appearance": {"gender": "Male", "height": ["6", "190 cm"]},
            "work": {"occupation": ""}
        },
        {
            "name": "Hero3",
            "appearance": {"gender": "Female", "height": ["5", "170 cm"]},
            "work": {"occupation": "Doctor"}
        },
        {
            "name": "Hero4",
            "appearance": {"gender": "Female", "height": ["5", "150 cm"]},
            "work": {"occupation": ""}
        }
    ]


# Заменяем функцию на подменную
# Функциональный тест: Самый высокий мужчина с работой
def test_tallest_male_with_work(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes)

    result = tallest_superhero("Male", True)

    assert result == "Hero1"

# Функциональный тест: Самый высокий мужчина без работы
def test_tallest_male_without_work(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes)

    result = tallest_superhero("Male", False)

    assert result == "Hero2"

# Функциональный тест: Самая высокая женщина с работой
def test_tallest_female_with_work(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes)

    result = tallest_superhero("Female", True)

    assert result == "Hero3"

# Функциональный тест: Самая высокая женщина без работы
def test_tallest_female_without_work(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes)

    result = tallest_superhero("Female", False)

    assert result == "Hero4"

# Функциональный тест: проверка на чуствительность регистра в гендере (мужчина)
def test_tallest_male_with_work_register(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes)

    result = tallest_superhero("MaLE", True)

    assert result == "Hero1"

# Функциональный тест: проверка на чуствительность регистра в гендере (женщина)
def test_tallest_female_without_work_register(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes)

    result = tallest_superhero("feMAle", False)

    assert result == "Hero4"

# негативные тесты
# Проверка, несуществующий гендер
def test_fake_gender(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes)

    result = tallest_superhero("Test", True)

    assert result == None

# Проверка, гендер не указан
def test_empty_gender(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes)

    result = tallest_superhero("", True)

    assert result == None

# Проверка, тип гендера None
def test_type_gender(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes)

    with pytest.raises(AttributeError):
        tallest_superhero(None, True)

# Проверка, типы данных в гендере и работе не соответствуют заявленным
def test_type_gender_and_work(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes)

    with pytest.raises(AttributeError):
        tallest_superhero(123, "123")