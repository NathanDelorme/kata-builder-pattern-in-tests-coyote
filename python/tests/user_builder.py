from shop import User, Address

class UserBuilder:
    def __init__(self) -> None:
        self._name = "Bob"
        self._email = "bob@domain.tld"
        self._age = 25
        self._address = Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA")
        self._verified = True

    def build(self) -> User:
        user = User(self._name, self._email, self._age, self._address, self._verified)
        self.__init__()
        return user

    def reset(self) -> None:
        self.__init__()

    def set_name(self, name: str) -> None:
        self._name = name

    def set_email(self, email: str) -> None:
        self._email = email

    def set_age(self, age: int) -> None:
        self._age = age

    def set_address(self, address: Address) -> None:
        self._address = address

    def set_verified(self, is_verified: bool) -> None:
        self._verified = is_verified
