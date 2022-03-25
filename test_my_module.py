import pytest
from my_module import greeting
from my_module import letter_text

def test_greeting_pass():
    assert "Hello, Carlos" == greeting("Carlos"), 'Test Failed'

def test_greeting_pass2():
        assert "Hello, Kitty" == greeting('Bacon'), 'Test Failed'

def test_letter_text():
    assert 'Hello Carlos, this letter is to inform you that you have won 7 Yen.' == letter_text(name = "Carlos", amount = "7", denomination = "Yen"), 'Test Failed'

def test_letter_text2():
    assert 'Hello Human, this letter is to inform you that you have won 100,000 StarPointz.' == letter_text(name = "Human", amount = "69", denomination = "StarPointz"), 'Test Failed'