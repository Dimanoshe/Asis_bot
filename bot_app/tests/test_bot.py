import os
import pytest
from ..bot_app import handle_message


def test_bot_app(message, expected):
    assert handle_message(message) == expected