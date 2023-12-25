from data import users
from pages.registration_page import RegistationPage
from selene import have


def test_form_submit_checker():
    registration_page = RegistationPage()

    registration_page.open()

    # WHEN
    registration_page.register(users.ivan)

    # THEN

    registration_page.registered_user_data.should(have.exact_texts('Ivan Ivanov',
                                                                   'ivanov@mail.com', 'Male', '8925239563',
                                                                   '01 June,1988',
                                                                   'English',
                                                                   'Reading', '1.jpeg', 'Leskova street,8',
                                                                   'Uttar Pradesh Agra'))
