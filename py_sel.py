# python_selenium_functions.py

import os


def create_python_selenium_project(project_directory):
    os.system(f"python -m venv {project_directory}/venv")
    os.system(f"{project_directory}/venv/bin/activate && pip install selenium pytest")

    os.makedirs(f"{project_directory}/tests", exist_ok=True)

    with open(f"{project_directory}/tests/test_example.py", "w") as test_file:
        test_file.write(
            """
import pytest
from selenium import webdriver

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_example(browser):
    browser.get("https://example.com")
    assert browser.title == "Example Domain"
"""
        )
