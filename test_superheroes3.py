import pytest
from main import tallest_superhero

# В данной подменной функции везде неправильные значения роста
def change_superheroes3():
    return [
        {
            "name": "Hero1",
            "appearance": {"gender": "Male", "height": ["5", None]},
            "work": {"occupation": "Engineer"}
        },
        {
            "name": "Hero2",
            "appearance": {"gender": "Male", "height": ["5", True]},
            "work": {"occupation": ""}
        },
        {
            "name": "Hero3",
            "appearance": {"gender": "Female", "height": ["5", False]},
            "work": {"occupation": "Engineer"}
        },
        {
            "name": "Hero4",
            "appearance": {"gender": "Male", "height": ["5", ""]},
            "work": {"occupation": "Engineer"}
        },
        {
            "name": "Hero5",
            "appearance": {"gender": "Female", "height": ["5", 123]},
            "work": {"occupation": ""}
        }
    ]

def test_male_false(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes3)

    with pytest.raises(AttributeError):
        tallest_superhero("Male", False)

def test_female_true(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes3)

    with pytest.raises(AttributeError):
        tallest_superhero("Female", True)

def test_type_gender_true_without_work1(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes3)

    with pytest.raises(AttributeError):
        tallest_superhero(True, True)

def test_type_gender_true_without_work2(monkeypatch):
    monkeypatch.setattr("main.all_superheroes", change_superheroes3)

    with pytest.raises(AttributeError):
        tallest_superhero(False, False)