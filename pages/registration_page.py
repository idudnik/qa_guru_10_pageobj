from pathlib import Path

from selene import browser, have, be, by
from selene.support.shared.jquery_style import s


class RegistationPage:
    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank)
        browser.element('#firstName').type(value)

    def fill_last_name(self, value):
        browser.element('#lastName').type(value)

    def fill_email(self, mail):
        browser.element('#userEmail').type(mail)

    def fill_gender(self, value):
        browser.all('[for*=gender-radio]').element_by(have.text(value)).click()

    def fill_mobile(self, value):
        browser.element('#userNumber').type(value)

    def fill_date_of_birth(self, year, month, day):
        s('#dateOfBirthInput').click()
        s('.react-datepicker__month-select').click().element(by.text(month)).click()
        s('.react-datepicker__year-select').click().element(by.text(year)).click()
        s(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        browser.element('#subjectsInput').type(value).press_enter()

    def fill_hobbie(self, value):
        browser.all('.custom-checkbox').element_by(have.exact_text(value)).click()

    def picture_upload(self, picture):
        picture_path = Path(__file__).parent.parent.joinpath('resources', picture)
        browser.element('#uploadPicture').send_keys(str(picture_path))

    def fill_address(self, value):
        browser.element('#currentAddress').type(value)

    def fill_state(self, value):
        browser.element('#react-select-3-input').type(value).press_enter()

    def fill_city(self, value):
        browser.element('#react-select-4-input').type(value).press_enter()

    def press_submit(self):
        browser.element('#submit').press_enter()

    def should_include_info(self, full_name, email, gender, mobile, date_of_bitrth, subject, hobbie, picture_name,
                            address, city_and_state):
        browser.all('tbody tr td:last-child').should(
            have.exact_texts(full_name, email, gender, mobile, date_of_bitrth, subject, hobbie, picture_name, address,
                             city_and_state))
