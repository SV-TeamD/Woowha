import os, json, pytest
from flask import Flask
from app import create_app


@pytest.fixture(autouse=True)
def client():
    app = create_app("test")
    with app.test_client() as client:
        yield client