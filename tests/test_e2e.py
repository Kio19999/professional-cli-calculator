import subprocess
import time
import requests
from playwright.sync_api import sync_playwright


def start_server():
    return subprocess.Popen(
        ["python", "-m", "uvicorn", "app.calculator.app:app", "--port", "8000"]
    )


def wait_for_server():
    for _ in range(10):
        try:
            requests.get("http://127.0.0.1:8000")
            return
        except:
            time.sleep(1)
    raise Exception("Server did not start")


def test_e2e_add():
    server = start_server()
    try:
        wait_for_server()

        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()

            page.goto("http://127.0.0.1:8000/add?a=2&b=3")
            content = page.content()

            assert "5" in content

            browser.close()

    finally:
        server.terminate()