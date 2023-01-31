from re import findall


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


class InvalidNameError(Exception):
    pass


pattern_name = r'[\w+\.]+'
pattern_domain = r'\.[a-z]+'

email = input()

MIN_LENGTH = 4
valid_domains = [".com", ".bg", ".net", ".org"]

while email != 'End':
    try:
        if email.count('@') > 1:
            raise MoreThanOneAtSymbolError('Email should contain only one "@" symbol!')
        if len(email.split('@')[0]) <= MIN_LENGTH:
            raise NameTooShortError(f'Name must be more than {MIN_LENGTH} characters')
        if findall(pattern_name, email)[0] != email.split("@")[0]:
            raise InvalidNameError("Name can only contain numbers, letters, underscores and dots.")
        if '@' not in email:
            raise MustContainAtSymbolError('Email must contain @"')
        if findall(pattern_domain, email)[-1] not in valid_domains:
            raise InvalidDomainError(f'Domain must be one of the following: {", ".join(valid_domains)}')

    except IndexError:
        print('Invalid email!')

    else:
        print('Email is valid')

    email = input()
