import dataclasses


@dataclasses.dataclass
class User:
    first_name: str
    last_name: str
    email: str
    gender: str
    mobile: int
    day_of_birth: str
    month_of_birth: str
    year_of_birth: str
    subject: str
    hobbie: str
    picture_name: str
    address: str
    state: str
    city: str


ivan = User(first_name='Ivan', last_name='Ivanov', email='ivanov@mail.com', gender='Male', mobile=8925239563,
            day_of_birth='11', month_of_birth='June', year_of_birth='1978',
            subject='English', hobbie='Reading', picture_name='1.jpeg', address='Leskova street,8',
            city='Agra', state='Uttar Pradesh')
