import requests

from unittest.mock import patch, Mock

from functions.pegar_versiculo import pegar_versiculo


HTML_FAKE = """
<html>
<body>

<div>[16] Sic enim Deus dilexit mundum</div>

<div>[17] Non enim misit Deus Filium</div>

</body>
</html>
"""


@patch("functions.pegar_versiculo.requests.get")
def test_fetch_single_verse(mock_get):

    response = Mock()

    response.status_code = 200
    response.text = HTML_FAKE

    mock_get.return_value = response

    resultado = pegar_versiculo(
        "evangelho segundo s. joão",
        "3",
        "16"
    )

    assert "[16]" in resultado