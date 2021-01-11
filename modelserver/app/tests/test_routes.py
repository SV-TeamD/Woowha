from flask import Flask
import pytest

from app.router import model_routes


class TestRoutes:
    def test_index_route(self, client):
        response = client.get("/")
        html = "model server index"
        assert response.data == html.encode()
        assert response.status_code == 200
