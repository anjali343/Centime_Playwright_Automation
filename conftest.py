import pytest
from playwright.sync_api import sync_playwright
from Utils.config import Config


def pytest_addoption(parser):
    parser.addoption(
        "--pw-browser",
        action="store",
        default=Config.DEFAULT_BROWSER,
        help="Browser to run tests against",
    )
    parser.addoption(
        "--pw-tracing",
        action="store_true",
        default=Config.DEFAULT_TRACING,
        help="Enable Playwright tracing",
    )


@pytest.fixture(scope="session")
def browser_name(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="session")
def tracing_enabled(request):
    return request.config.getoption("--tracing")


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="session")
def browser(playwright_instance, browser_name):
    browser = getattr(playwright_instance, browser_name).launch(headless=Config.HEADED)
    yield browser
    browser.close()


@pytest.fixture()
def page(browser, request, tracing_enabled):
    context = browser.new_context(viewport={"width": 1520, "height": 1080})
    if tracing_enabled:
        context.tracing.start()

    page = context.new_page()
    page.goto(Config.BASE_URL)
    yield page

    if tracing_enabled:
        context.tracing.stop(path='NormalReports/trace.zip')
    context.close()
