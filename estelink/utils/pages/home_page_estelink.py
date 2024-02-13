import allure


class HomeEstelinkPage:
    def __init__(self, page):
        self.page = page

    @allure.step("Выбираем кнопку Авторизация на главной странице")
    async def click_authorization_button(self):
        self.page.get_by_role("button", name="").click()

    @allure.step("Выбираем кнопку Регистрация на главной странице")
    async def click_registration_button(self):
        self.page.get_by_role("button", name="Регистрация").click()


class AuthorizationPage:
    @allure.step("Создаем объект класса Авторизация")
    def __init__(self, page):
        self.page = page

    @allure.step("Вводим логин для авторизации")
    async def fill_email_input(self, string):
        self.page.locator("input[type=\"text\"]").fill(string)
        return self

    @allure.step("Вводим пароль для авторизации")
    async def fill_password_input(self, string):
        self.page.locator("input[type=\"password\"]").fill(string)
        return self

    @allure.step("Нажимаем кнопку для сохранения введенных данных")
    async def click_entry_button(self):
        self.page.get_by_role("button", name="Войти в систему").click()
        return self

    @allure.step("Кликаем на нужный филиал")
    async def click_filial_button(self):
        self.page.get_by_role("button", name="").click()
        return self
