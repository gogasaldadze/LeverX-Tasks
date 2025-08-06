from dataclasses import dataclass, field
from typing import Tuple
import re


@dataclass(order=True)
class Version:
    comparison_field: Tuple = field(init=False, repr=False)
    comparison_object: str = field(compare=False)

    RELEASE = 1
    PRERELEASE = 0
    STRING = 1
    NUMERIC = 0

    acceptable_pattern = re.compile(
        r"^(?P<major>0|[1-9]\d*)\."
        r"(?P<minor>0|[1-9]\d*)\."
        r"(?P<patch>0|[1-9]\d*)"
        r"(?:-(?P<prerelease>[0-9A-Za-z.-]+))?"
        r"(?:\+(?P<buildmetadata>[0-9A-Za-z.-]+))?$"
    )

    def __post_init__(self):
        normalized = self.normalization()
        match = self.acceptable_pattern.match(normalized)

        if not match:
            raise ValueError(f"Invalid Semantic version {self.comparison_object}")

        # matching major/minor/patch/prerelease

        major = int(match.group("major"))
        minor = int(match.group("minor"))
        patch = int(match.group("patch"))
        prerelease = match.group("prerelease")

        normalized_prerelease = self.parse_prerelease(prerelease)

        # This field is used for ordering/comparison of version objects
        self.comparison_field = (major, minor, patch, normalized_prerelease)

    def normalization(self):
        """
        Normalizes version strings to standard SemVer format.
        1. Ensures hyphen before prerelease (1.0.0alpha -> 1.0.0-alpha)
        2. Converts letters to lowercase
        3. Preserves existing hyphens and dots

        """

        new = ""

        for char in self.comparison_object:
            if char.isalpha():
                if new and new[-1].isdigit():
                    new += "-"
                new += char.lower()
            else:
                new += char

        return new

    def parse_prerelease(self, prerelease):
        """
        Parses the prerelease string into a structured format.
        Rules:
            if no prerelease presented, its considered as a full release (therefore RELEASE = 1)
            otherwise, split prerelease by "." (if presented) or digit boundaries.
            lastly, each component is marked as numeric or string for comparison purposes .

            Examples:
            'alpha.1' -> (PRERELEASE, [(STRING, 'alpha'), (NUMERIC, 1)])
            'rc1'     -> (PRERELEASE, [(STRING, 'rc'), (NUMERIC, 1)])
            None      -> (RELEASE, ())
        """
        if prerelease is None:
            return (self.RELEASE, ())

        if "." in prerelease:
            parts = prerelease.split(".")

        else:
            parts = re.split(r"(?<=\D)(?=\d)", prerelease)

        components = list()

        for part in parts:

            if part.isdigit():
                components.append(((self.NUMERIC, int(part))))
            else:
                components.append((self.STRING, part.lower()))

        return (self.PRERELEASE, tuple(components))
