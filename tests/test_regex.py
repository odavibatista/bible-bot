import re

PATTERN = r'^(.+) (\d+),(\d+)(-(\d+))?$'


def test_single_verse():
    match = re.match(
        PATTERN,
        "gênesis 1,1"
    )

    assert match is not None

    nome, cap, vers_inicio, _, vers_fim = match.groups()

    assert nome == "gênesis"
    assert cap == "1"
    assert vers_inicio == "1"
    assert vers_fim is None


def test_verse_range():
    match = re.match(
        PATTERN,
        "joão 3,16-18"
    )

    assert match is not None

    nome, cap, vers_inicio, _, vers_fim = match.groups()

    assert nome == "joão"
    assert cap == "3"
    assert vers_inicio == "16"
    assert vers_fim == "18"


def test_invalid_reference():
    match = re.match(
        PATTERN,
        "joão abc"
    )

    assert match is None