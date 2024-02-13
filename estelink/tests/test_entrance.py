import os
import pytest
from dotenv import load_dotenv
from playwright.async_api import expect

from estelink.utils.pages.home_page_estelink import HomeEstelinkPage, AuthorizationPage

from allure import (
    title,
    feature,
    tag,
    severity,
    severity_level
)

load_dotenv()


def perform_login(page):
    page.goto(os.getenv('BASE_URL'))
    main_page = HomeEstelinkPage(page)
    main_page.click_authorization_button()

    authorization_page = AuthorizationPage(page)
    authorization_page.fill_email_input(os.getenv('E_MAIL')) \
        .fill_password_input(os.getenv('PASSWORD')) \
        .click_entry_button() \
        .click_filial_button()


@feature('Home')
@pytest.mark.regress
@pytest.mark.home
class TestEntrance:

    @title("Вход в Эстелинк")
    @tag("positive")
    @severity(severity_level.NORMAL)
    async def test_open_(self, page):
        perform_login(page)
        expect(page.get_by_text("Личные данные")).to_be_visible()
