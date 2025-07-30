import pytest
from main import tallest_superhero

# Подменяем функцию, чтобы не использовать настоящие данные
def change_superheroes2():
    return [
        {
            "name": "Hero1",
            "appearance": {"gender": "", "height": ["5", "180 cm"]},
            "work": {"occupation": "Engineer"}
        },
        {
            "name": "Hero2",
            "appearance": {"gender": "Male", "height": ["5", ""]},
            "work": {"occupation": "Doctor"}
        },
        {
            "name": "Hero3",
            "appearance": {"gender": "Female", "height": ["5", "160 cm"]},
            "work": {"occupation": ""}
        },
        {
            "name": "Hero4",
            "appearance": {"gender": "Female", "height": ["5", "170 cm"]},
            "work": {"occupation": ""}
        }
        ]

# В функции нет данных о росте мужчин
def test_male_without_height(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes2)

    result = tallest_superhero("Male", True)

    assert result == None

# Корректность работы при двух отфильтрованных значениях
def test_2_female(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes2)

    result = tallest_superhero("Female", False)

    assert result == "Hero4"

# Нет подходящих значений
def test_female_with_work(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes2)

    result = tallest_superhero("Female", True)

    assert result == None
