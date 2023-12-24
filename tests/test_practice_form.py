from data import users
from data.users import ivan
from pages.registration_page import RegistationPage
from selene import have

def test_form_submit_checker():
    registration_page = RegistationPage()
    ivan=users.ivan

    registration_page.open()

    # WHEN
    registration_page.register(users.ivan)

    registration_page.fill_first_name(ivan.first_name)
    registration_page.fill_last_name(ivan.last_name)
    registration_page.fill_email(ivan.email)
    registration_page.fill_gender(ivan.gender)
    registration_page.fill_mobile(ivan.mobile)
    registration_page.fill_date_of_birth(ivan.day_of_birth,ivan.month_of_birth ,ivan.year_of_birth)
    registration_page.fill_subject(ivan.subject)
    registration_page.fill_hobbie(ivan.hobbie)
    registration_page.picture_upload(ivan.picture_name)
    registration_page.fill_address(ivan.address)
    registration_page.fill_state(ivan.city)
    registration_page.fill_city(ivan.state)
    registration_page.press_submit()

    # THEN

    registration_page.registered_user_data.should(have.exact_texts('Ivan Ivanov',
                                                                   'ivanov@mail.com', 'Male', '8925239563',
                                                                   '01 June,1988',
                                                                   'English',
                                                                   'Reading', '1.jpeg', 'Leskova street,8',
                                                                   'Uttar Pradesh Agra'))

    # registration_page.should_include_info('Ivan Ivanov',
    #                                       'ivanov@mail.com', 'Male', '8925239563',
    #                                       '01 June,1988',
    #                                       'English',
    #                                       'Reading', '1.jpeg', 'Leskova street,8',
    #                                       'Uttar Pradesh Agra')
