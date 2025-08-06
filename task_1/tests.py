import unittest
from main import Version


class VersionTest(unittest.TestCase):

    def test_equal_versions(self):
        self.assertEqual(Version("1.0.0"), Version("1.0.0"))
        self.assertEqual(Version("1.0.0-alpha"), Version("1.0.0alpha"))
        self.assertEqual(Version("1.0.0-alpha.1"), Version("1.0.0alpha.1"))
        self.assertEqual(Version("1.0.0-alpha23"), Version("1.0.0-alpha23"))

    def test_less_than(self):
        # Basic version comparison
        self.assertLess(Version("1.0.0"), Version("2.0.0"))
        self.assertLess(Version("1.0.0"), Version("1.1.0"))
        self.assertLess(Version("1.0.0"), Version("1.0.1"))

        # Prerelease comparisons
        self.assertLess(Version("1.0.0-alpha"), Version("1.0.0"))
        self.assertLess(Version("1.0.0-alpha"), Version("1.0.0-beta"))
        self.assertLess(Version("1.0.0-alpha.1"), Version("1.0.0-alpha.2"))

        # Numeric suffix comparison
        self.assertLess(Version("1.0.0alpha1"), Version("1.0.0alpha2"))
        self.assertLess(Version("1.0.0alpha23"), Version("1.0.0alpha100"))

        # Mixed comparisons
        self.assertLess(Version("1.0.0-alpha23"), Version("1.0.0-rc.1"))
        self.assertLess(Version("1.0.0-alpha"), Version("1.0.0-alpha.1"))

    def test_greater_than(self):
        self.assertGreater(Version("2.0.0"), Version("1.0.0"))
        self.assertGreater(Version("1.0.0"), Version("1.0.0-alpha"))
        self.assertGreater(Version("1.0.0-beta"), Version("1.0.0-alpha"))
        self.assertGreater(Version("1.0.0-alpha.2"), Version("1.0.0-alpha.1"))

    def test_special_cases(self):
        # Numeric vs string components
        self.assertLess(Version("1.0.0-1"), Version("1.0.0-alpha"))
        self.assertLess(Version("1.0.0-1alpha"), Version("1.0.0-1beta"))

        # Complex prereleases
        self.assertLess(Version("1.0.0-alpha.1"), Version("1.0.0-alpha.1.1"))
        self.assertLess(Version("1.0.0-alpha.1.beta"), Version("1.0.0-alpha.1.gamma"))

    def test_invalid_versions(self):
        with self.assertRaises(ValueError):
            Version("1.0")
        with self.assertRaises(ValueError):
            Version("1.0.0.0")
        with self.assertRaises(ValueError):
            Version("1.0.0-")


if __name__ == "__main__":
    unittest.main()
