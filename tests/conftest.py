import pytest
import httpretty


@pytest.fixture(scope="session", autouse=True)
def run_first():
    httpretty.enable()
