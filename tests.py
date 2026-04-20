import unittest

from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):
    def test_visa_valid_standard(self):
        """Verifies a standard valid Visa number returns True
        Picked using Partition Testing for a valid Visa partition"""
        self.assertTrue(credit_card_validator("4111111111111111"))

    def test_visa_valid_all_zero_body(self):
        """Verifies another valid Visa number returns True
        Picked using Partition Testing to cover a different valid Visa value"""
        self.assertTrue(credit_card_validator("4000000000000002"))

    def test_visa_invalid_check_digit(self):
        """Verifies Visa with valid prefix and length but invalid check digit returns False
        Picked using Partition Testing by toggling only the checksum"""
        self.assertFalse(credit_card_validator("4111111111111112"))

    def test_visa_invalid_short_length(self):
        """Verifies Visa with prefix 4 and length 15 returns False
        Picked using Boundary Value Testing just below the valid Visa length"""
        self.assertFalse(credit_card_validator("400000000000006"))

    def test_visa_invalid_long_length(self):
        """Verifies Visa with prefix 4 and length 17 returns False
        Picked using Boundary Value Testing just above the valid Visa length"""
        self.assertFalse(credit_card_validator("40000000000000006"))

    def test_mastercard_valid_lower_prefix_boundary(self):
        """Verifies MasterCard prefix 51 is accepted
        Picked using Boundary Value Testing at the lower bound of the 51-55 range"""
        self.assertTrue(credit_card_validator("5100000000000008"))

    def test_mastercard_valid_upper_prefix_boundary(self):
        """Verifies MasterCard prefix 55 is accepted
        Picked using Boundary Value Testing at the upper bound of the 51-55 range"""
        self.assertTrue(credit_card_validator("5500000000000004"))

    def test_mastercard_invalid_above_55_prefix(self):
        """Verifies prefix 56 is rejected for MasterCard
        Picked using Boundary Value Testing just above the 51-55 range"""
        self.assertFalse(credit_card_validator("5600000000000003"))

    def test_mastercard_invalid_below_51_prefix(self):
        """Verifies prefix 50 is rejected for MasterCard
        Picked using Boundary Value Testing just below the 51-55 range"""
        self.assertFalse(credit_card_validator("5000000000000009"))

    def test_mastercard_valid_lower_4_digit_range(self):
        """Verifies MasterCard prefix 2221 is accepted
        Picked using Boundary Value Testing at the lower bound of the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2221000000000009"))

    def test_mastercard_valid_upper_4_digit_range(self):
        """Verifies MasterCard prefix 2720 is accepted
        Picked using Boundary Value Testing at the upper bound of the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2720000000000005"))

    def test_mastercard_invalid_below_2221_prefix(self):
        """Verifies prefix 2220 is rejected for MasterCard
        Picked using Boundary Value Testing just below the 2221-2720 range"""
        self.assertFalse(credit_card_validator("2220000000000000"))

    def test_mastercard_invalid_above_2720_prefix(self):
        """Verifies prefix 2721 is rejected for MasterCard
        Picked using Boundary Value Testing just above the 2221-2720 range"""
        self.assertFalse(credit_card_validator("2721000000000004"))

    def test_mastercard_invalid_check_digit_51_range(self):
        """Verifies MasterCard with valid 51 prefix and length but invalid check digit returns False
        Picked using Partition Testing by changing only the checksum"""
        self.assertFalse(credit_card_validator("5100000000000009"))

    def test_mastercard_invalid_short_length(self):
        """Verifies MasterCard with valid prefix and length 15 returns False
        Picked using Boundary Value Testing just below the valid MasterCard length"""
        self.assertFalse(credit_card_validator("510000000000003"))

    def test_mastercard_invalid_long_length(self):
        """Verifies MasterCard with valid prefix and length 17 returns False
        Picked using Boundary Value Testing just above the valid MasterCard length"""
        self.assertFalse(credit_card_validator("51000000000000003"))

    def test_amex_valid_prefix_34(self):
        """Verifies American Express prefix 34 with valid length and checksum returns True
        Picked using Partition Testing for a valid AmEx partition"""
        self.assertTrue(credit_card_validator("340000000000009"))

    def test_amex_valid_prefix_37(self):
        """Verifies American Express prefix 37 with valid length and checksum returns True
        Picked using Partition Testing for the second valid AmEx prefix partition"""
        self.assertTrue(credit_card_validator("370000000000002"))

    def test_amex_invalid_prefix_33(self):
        """Verifies prefix 33 is rejected for American Express
        Picked using Boundary Value Testing just below valid AmEx prefix 34"""
        self.assertFalse(credit_card_validator("330000000000001"))

    def test_amex_invalid_prefix_38(self):
        """Verifies prefix 38 is rejected for American Express
        Picked using Boundary Value Testing just above valid AmEx prefix 37"""
        self.assertFalse(credit_card_validator("380000000000000"))

    def test_amex_invalid_check_digit(self):
        """Verifies American Express with valid prefix and length but invalid check digit returns False
        Picked using Partition Testing by changing only the checksum"""
        self.assertFalse(credit_card_validator("340000000000008"))

    def test_amex_invalid_short_length(self):
        """Verifies American Express with valid prefix and length 14 returns False
        Picked using Boundary Value Testing just below the valid AmEx length"""
        self.assertFalse(credit_card_validator("34000000000000"))

    def test_amex_invalid_long_length(self):
        """Verifies American Express with valid prefix and length 16 returns False
        Picked using Boundary Value Testing just above the valid AmEx length"""
        self.assertFalse(credit_card_validator("3400000000000000"))

    def test_invalid_prefix_with_valid_length_and_checksum(self):
        """Verifies a number with invalid issuer prefix but valid length and checksum returns False
        Picked using Error Guessing to catch implementations that only check Luhn and length"""
        self.assertFalse(credit_card_validator("6011000000000004"))

    def test_invalid_everything(self):
        """Verifies a number with invalid prefix, invalid length, and invalid checksum returns False
        Picked using Error Guessing to test a clearly invalid combination"""
        self.assertFalse(credit_card_validator("123456789012"))

    def test_visa_valid_prefix_not_mastercard(self):
        """Verifies a valid Visa is not rejected because it is not MasterCard or AmEx
        Picked using Partition Testing to ensure issuer partitions are kept separate"""
        self.assertTrue(credit_card_validator("4000000000000002"))

    def test_mastercard_2221_invalid_check_digit(self):
        """Verifies MasterCard prefix 2221 with invalid checksum returns False
        Picked using Partition Testing on the 2221-2720 range specifically"""
        self.assertFalse(credit_card_validator("2221000000000008"))

    def test_mastercard_2720_invalid_check_digit(self):
        """Verifies MasterCard prefix 2720 with invalid checksum returns False
        Picked using Partition Testing on the upper boundary of the 2221-2720 range"""
        self.assertFalse(credit_card_validator("2720000000000004"))

    def test_amex_37_invalid_check_digit(self):
        """Verifies AmEx prefix 37 with invalid checksum returns False
        Picked using Partition Testing on the second AmEx prefix"""
        self.assertFalse(credit_card_validator("370000000000003"))

    def test_visa_invalid_prefix_like_3_series(self):
        """Verifies a 15-digit card from the 3-series that is not 34 or 37 returns False
        Picked using Error Guessing to catch over-broad American Express prefix checks"""
        self.assertFalse(credit_card_validator("360000000000008"))


if __name__ == '__main__':
    unittest.main()