import pytest
from playwright.sync_api import sync_playwright, Page, expect
from page.page_test import *
from config.conftest import *


@pytest.mark.smoke
def test_flow(page, tp_template_login, tp_template):
    tp_template_login()
    tp_template()
