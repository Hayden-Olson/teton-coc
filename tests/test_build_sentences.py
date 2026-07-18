import pytest
import json
from build_sentences import (get_seven_letter_word, parse_json_from_file, choose_sentence_structure,
                              get_pronoun, get_article, get_word, fix_agreement, build_sentence, structures)

def test_get_seven_letter_word(mocker):
    mock_input = mocker.patch("builtins.input",return_value = "imagine")
    assert get_seven_letter_word() == "IMAGINE"
    mock_input = mocker.patch("builtins.input",return_value = "character")
    assert get_seven_letter_word() == "CHARACTER"
    mock_input = mocker.patch("builtins.input",return_value = "pop")
    with pytest.raises(ValueError):
        get_seven_letter_word()
    mock_input.assert_called_once()
    

def test_parse_json_from_file(tmp_path):
    content = {'1':"spongebob"}
    test_data = json.dumps(content)
    file_path = tmp_path / "test.json"
    with open(file_path, "w") as f:
        f.write(test_data)
    assert parse_json_from_file(file_path) == content
    
    test_data = '{1:"spongebob",}'
    file_path = tmp_path / "test.json"
    with open(file_path, "w") as f:
        f.write(test_data)
    with pytest.raises(json.JSONDecodeError):
        parse_json_from_file(file_path)
        
    file_path = tmp_path / "test1"
    with pytest.raises(FileNotFoundError):
        parse_json_from_file(file_path)
    

def test_choose_sentence_structure(mocker):
    mock_choice = mocker.patch("random.choice",return_value=structures[0])
    assert choose_sentence_structure() == structures[0]

def test_get_pronoun(mocker):
    mock_choice = mocker.patch("random.choice", return_value="he")
    assert get_pronoun() == "he"

def test_get_article(mocker):
    mock_choice = mocker.patch("random.choice",return_value="a")
    assert get_article() == "a"

def test_get_word():
    assert get_word("A",["apple","peanut", "zoologist"]) == "apple"
    assert get_word("C",["apple","peanut", "zoologist"]) == "zoologist"
    with pytest.raises(IndexError):
        get_word("D",["apple","peanut", "zoologist"])

def test_fix_agreement():
    sentence = "Jane ate a apple.".split()
    fix_agreement(sentence)
    assert " ".join(sentence) == "Jane ate an apple."
    
    sentence = "she quickly skip to school.".split()
    fix_agreement(sentence)
    assert " ".join(sentence) == "she quickly skips to school."
    
    sentence = "the purple dog frantically chase the squirrel.".split()
    fix_agreement(sentence)
    assert " ".join(sentence) == "the purple dog frantically chases the squirrel."
    
    sentence = "the purple dog frantically chase the squirrel, and Jane eats a apple as she quickly skip to school.".split()
    fix_agreement(sentence)
    assert " ".join(sentence) == "the purple dog frantically chases the squirrel, and Jane eats an apple as she quickly skips to school."

def test_build_sentence(mocker):
    data = {"adjectives": ["purple","prickly","scenic"],
            "nouns": ["pineapple","chair","pizza"],
            "verbs": ["run","eating","gallop"],
            "adverbs": ["quickly","sporadically","slowly"],
            "prepositions": ["under","over","though"]}
    seed = "BACCAAB"
    structure = ["ART","ADJ","NOUN","ADV","VERB","PREP","ART","ADJ","NOUN"]
    mock_choice = mocker.patch("build_sentences.get_article",return_value="the")
    assert build_sentence(seed,structure,data) == "The prickly pineapple slowly gallops under the purple chair"
    seed = "ABCABCA"
    assert build_sentence(seed,structure,data) == "The purple chair slowly runs over the scenic pineapple"