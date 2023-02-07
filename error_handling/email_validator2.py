class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


email = input()

MIN_LENGTH = 4
valid_domains = [".com", ".bg", ".net", ".org"]

while email != "End":

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    name, domain = email.split('@')

    if len(name) <= MIN_LENGTH:
        raise NameTooShortError(f"Name must be more than {MIN_LENGTH} characters")

    if not any(email.endswith(x) for x in valid_domains):
        raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')

    print('Email s valid')

    email = input()
