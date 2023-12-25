from pages.registration_page import RegistationPage

from data.users import ivan


def test_form_submit_checker():
    registration_page = RegistationPage()

    registration_page.open()

    # WHEN
    registration_page.register(ivan)

    # THEN

    registration_page.user_register_form(ivan)