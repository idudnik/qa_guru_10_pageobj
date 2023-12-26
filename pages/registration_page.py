from pathlib import Path

from selene import browser, have, be, by, command

from data.users import User
from selene.support.shared.jquery_style import s


class RegistationPage:
    def __init__(self):
        self.first_name = browser.element('#firstName')
        self.last_name = browser.element('#lastName')
        self.email = browser.element('#userEmail')
        self.gender = browser.all('[for*=gender-radio]')
        self.mobile = browser.element('#userNumber')
        self.date_of_birth = browser.element('#dateOfBirthInput')
        self.month_of_birth = browser.element('.react-datepicker__month-select')
        self.year_of_birth = browser.element('.react-datepicker__year-select')
        self.subject = browser.element('#subjectsInput')
        self.hobbie = browser.all('.custom-checkbox')
        self.picture = browser.element('#uploadPicture')
        self.address = browser.element('#currentAddress')
        self.city = s('#react-select-4-input')

        self.state = s('#react-select-3-input')

        self.submit = browser.element('#submit')

        self.registered_user_data = browser.all('tbody tr td:last-child')

    def open(self):
        browser.open("/automation-practice-form")

    def fill_first_name(self, value):
        self.first_name.type(value)

    def fill_last_name(self, value):
        self.last_name.type(value)

    def fill_email(self, mail):
        self.email.type(mail)

    def fill_gender(self, value):
        self.gender.element_by(have.text(value)).click()

    def fill_mobile(self, value):
        self.mobile.type(value)

    def fill_date_of_birth(self, month, year, day):
        self.date_of_birth.perform(command.js.scroll_into_view)
        self.date_of_birth.click()
        self.month_of_birth.click().element(by.text(month)).click()
        self.year_of_birth.click().element(by.text(year)).click()
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subject(self, value):
        self.subject.type(value).press_enter()

    def fill_hobbie(self, value):
        self.hobbie.element_by(have.exact_text(value)).click()

    def picture_upload(self, picture):
        picture_path = Path(__file__).parent.parent.joinpath('resources', picture)
        self.picture.send_keys(str(picture_path))

    def fill_address(self, value):
        self.address.type(value)

    def fill_state(self, value):
        self.state.should(be.blank).type(value).press_enter()

    def fill_city(self, value):
        self.city.should(be.blank).type(value).press_enter()

    def press_submit(self):
        self.submit.press_enter()

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_last_name(user.last_name)
        self.fill_email(user.email)
        self.fill_gender(user.gender)
        self.fill_mobile(user.mobile)
        self.fill_date_of_birth(user.month_of_birth, user.year_of_birth, user.day_of_birth)
        self.fill_subject(user.subject)
        self.fill_hobbie(user.hobbie)
        self.picture_upload(user.picture_name)
        self.fill_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)
        self.press_submit()

    def user_register_form(self, user):
        browser.all('.table-responsive').all('td').should(have.exact_texts
            (
            f'{user.first_name} {user.last_name}',

            user.email,
            user.gender,
            str(user.mobile),
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            user.subject,
            user.hobbie,
            user.picture_name,
            user.address,
            f'{user.state} {user.city}'
        )
        )
