import pytest
from pole_chudes import PoleChudes

def test_game_class_creation():
    game = PoleChudes("питон")
    assert game is not None

def test_guess_letter():
    game = PoleChudes("питон")
    assert game.guess_letter("п") == ["П", "_", "_", "_", "_"]
    assert game.guess_letter("н") == ["П", "_", "_", "_", "Н"]
    assert game.guess_letter("ы") == ["П", "_", "_", "_", "Н"]

def test_guess_word():
    game = PoleChudes("питон")
    assert game.guess_word("питон") is True
    assert game.guessed_word == ["П", "И", "Т", "О", "Н"]