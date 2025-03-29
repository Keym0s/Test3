import pytest
from pole_chudes import PoleChudes  #Пока этого модуля нет

def test_game_class_creation():
    game = PoleChudes("питон")
    assert game is not None

