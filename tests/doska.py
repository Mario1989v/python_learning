# -*- coding: utf-8 -*-
import pytest

from fixture.application import Application
from model.search_item import Theword


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_doska(app):
    app.open_homepage()
    app.search_kw(Theword("iphone"))
    app.select_first()








