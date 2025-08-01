from dataclasses import dataclass, field
from typing import Tuple
import re


@dataclass(order=True)   # basically initializing comparison dunder methods just by setting order=True
class Version:
    comparison_field: Tuple = field(init=False, repr=False)      
    comparison_object: str

    acceptable_pattern = re.compile(    # Suggested Regex found in FAQ: https://regex101.com/r/Ly7O1x/3 
        r"^(?P<major>0|[1-9]\d*)\."
        r"(?P<minor>0|[1-9]\d*)\."
        r"(?P<patch>0|[1-9]\d*)"
        r"(?:-(?P<prerelease>[0-9A-Za-z.-]+))?"
        r"(?:\+(?P<buildmetadata>[0-9A-Za-z.-]+))?$"
    )

    def __post_init__(self):
        normalized = self.normalization()   # no need to provide self.comparison_object, because i already did it in normalization() method.
        match = self.acceptable_pattern.match(normalized)

        if not match:
            raise ValueError (f'Invalid Semantic version {self.comparison_object}')
        
        # matching major/minor/patch/prerelease

        major = int(match.group('major'))
        minor = int(match.group('minor'))
        patch = int(match.group('patch'))
        prerelease = match.group('prerelease')

        normalized_prerelease = prerelease if prerelease is not None else 'z'  # assigned 'z' so its always higher than any prerelase char  (release > prerelease, eg:1.0.0-alpha, 1.0.0-beta )
        self.comparison_field = (major, minor, patch, normalized_prerelease)


    def normalization(self):
        new = ''

        for char in self.comparison_object:   
            if char.isalpha():
                if new and new[-1].isdigit():  # tryna check if new is not empty alongside with if the last existed char is digit
                    new += '-'
                new += char.lower() 
            else:
                new += char

        return new


# print(Version('1.1.3') < Version('2.2.3'))
# print(Version('1.3.0') > Version('0.3.0'))
# print(Version('0.3.0b') < Version('1.2.42'))
# print(Version('1.3.42') == Version('42.3.1'))

def main():
    to_test = [
        ("1.0.0", "2.0.0"),
        ("1.0.0", "1.42.0"),
        ("1.2.0", "1.2.42"),
        ("1.1.0-alpha", "1.2.0-alpha.1"),
        ("1.0.1b", "1.0.10-alpha.beta"),
        ("1.0.0-rc.1", "1.0.0"),
    ]

    for left, right in to_test:
        assert Version(left) < Version(right), "le failed"
        assert Version(right) > Version(left), "ge failed"
        assert Version(right) != Version(left), "neq failed"

    print('all tests passed')

if __name__ == "__main__":
    main()