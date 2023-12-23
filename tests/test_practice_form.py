from pages.registration_page import RegistationPage


def test_form_submit_checker():
    registration_page = RegistationPage()
    registration_page.open()

    # WHEN

    registration_page.fill_first_name('Ivan')
    registration_page.fill_last_name('Ivanov')
    registration_page.fill_email('ivanov@mail.com')
    registration_page.fill_gender('Male')
    registration_page.fill_mobile('8925239563')
    registration_page.fill_date_of_birth('1988', 'June', '01')
    registration_page.fill_subject('English')
    registration_page.fill_hobbie('Reading')
    registration_page.picture_upload('1.jpeg')
    registration_page.fill_address('Leskova street,8')
    registration_page.fill_state('Uttar Pradesh')
    registration_page.fill_city('Agra')
    registration_page.press_submit()

    # THEN
    registration_page.should_include_info('Ivan Ivanov',
                                          'ivanov@mail.com', 'Male', '8925239563',
                                          '01 June,1988',
                                          'English',
                                          'Reading', '1.jpeg', 'Leskova street,8',
                                          'Uttar Pradesh Agra')
