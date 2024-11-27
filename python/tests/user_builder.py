from shop import User, Address

class UserBuilder:
    def __init__(self) -> None:
        self._name = "Bob"
        self._email = "bob@domain.tld"
        self._age = 25
        self._address = Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA")
        self._verified = True

    def build(self) -> User:
        return User(self._name, self._email, self._age, self._address, self._verified)

    def minor(self):
        self._age = 15
        return self

    def not_verified(self):
        self._verified = False
        return self

    def foreign(self):
        self._address = Address("33 quai d'Orsay", "", "Paris", "75007", "France")
        return self


