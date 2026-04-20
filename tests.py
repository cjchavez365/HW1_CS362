import unittest

from credit_card_validator import credit_card_validator


class TestCreditCardValidator(unittest.TestCase):

    def test1(self):
        """Verifies a standard valid Visa number returns True
        Picked using Partition Testing for a valid Visa partition"""
        self.assertTrue(credit_card_validator("4111111111111111"))

    def test2(self):
        """Verifies another valid Visa number returns True
        Picked using Partition Testing to cover a different valid Visa value"""
        self.assertTrue(credit_card_validator("4000000000000002"))

    def test3(self):
        """Verifies Visa with valid prefix and length but invalid check digit returns False
        Picked using Partition Testing by toggling only the checksum"""
        self.assertFalse(credit_card_validator("4111111111111112"))

    def test4(self):
        """Verifies Visa with prefix 4 and length 15 returns False
        Picked using Boundary Value Testing just below the valid Visa length"""
        self.assertFalse(credit_card_validator("400000000000006"))

    def test5(self):
        """Verifies Visa with prefix 4 and length 17 returns False
        Picked using Boundary Value Testing just above the valid Visa length"""
        self.assertFalse(credit_card_validator("40000000000000006"))

    def test6(self):
        """Verifies MasterCard prefix 51 is accepted
        Picked using Boundary Value Testing at the lower bound"""
        self.assertTrue(credit_card_validator("5100000000000008"))

    def test7(self):
        """Verifies MasterCard prefix 55 is accepted
        Picked using Boundary Value Testing at the upper bound"""
        self.assertTrue(credit_card_validator("5500000000000004"))

    def test8(self):
        """Verifies prefix 56 is rejected
        Picked using Boundary Value Testing just above valid range"""
        self.assertFalse(credit_card_validator("5600000000000003"))

    def test9(self):
        """Verifies prefix 50 is rejected
        Picked using Boundary Value Testing just below valid range"""
        self.assertFalse(credit_card_validator("5000000000000009"))

    def test10(self):
        """Verifies MasterCard prefix 2221 is accepted
        Picked using Boundary Value Testing at lower bound"""
        self.assertTrue(credit_card_validator("2221000000000009"))

    def test11(self):
        """Verifies MasterCard prefix 2720 is accepted
        Picked using Boundary Value Testing at upper bound"""
        self.assertTrue(credit_card_validator("2720000000000005"))

    def test12(self):
        """Verifies prefix 2220 is rejected
        Picked using Boundary Value Testing below valid range"""
        self.assertFalse(credit_card_validator("2220000000000000"))

    def test13(self):
        """Verifies prefix 2721 is rejected
        Picked using Boundary Value Testing above valid range"""
        self.assertFalse(credit_card_validator("2721000000000004"))

    def test14(self):
        """Verifies MasterCard valid prefix but invalid check digit returns False
        Picked using Partition Testing"""
        self.assertFalse(credit_card_validator("5100000000000009"))

    def test15(self):
        """Verifies MasterCard length 15 is invalid
        Picked using Boundary Value Testing"""
        self.assertFalse(credit_card_validator("510000000000003"))

    def test16(self):
        """Verifies MasterCard length 17 is invalid
        Picked using Boundary Value Testing"""
        self.assertFalse(credit_card_validator("51000000000000003"))

    def test17(self):
        """Verifies AmEx prefix 34 valid case
        Picked using Partition Testing"""
        self.assertTrue(credit_card_validator("340000000000009"))

    def test18(self):
        """Verifies AmEx prefix 37 valid case
        Picked using Partition Testing"""
        self.assertTrue(credit_card_validator("370000000000002"))

    def test19(self):
        """Verifies prefix 33 is invalid for AmEx
        Picked using Boundary Value Testing"""
        self.assertFalse(credit_card_validator("330000000000001"))

    def test20(self):
        """Verifies prefix 38 is invalid for AmEx
        Picked using Boundary Value Testing"""
        self.assertFalse(credit_card_validator("380000000000000"))

    def test21(self):
        """Verifies AmEx invalid check digit
        Picked using Partition Testing"""
        self.assertFalse(credit_card_validator("340000000000008"))

    def test22(self):
        """Verifies AmEx length 14 is invalid
        Picked using Boundary Value Testing"""
        self.assertFalse(credit_card_validator("34000000000000"))

    def test23(self):
        """Verifies AmEx length 16 is invalid
        Picked using Boundary Value Testing"""
        self.assertFalse(credit_card_validator("3400000000000000"))

    def test24(self):
        """Verifies invalid prefix with valid length/checksum returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("6011000000000004"))

    def test25(self):
        """Verifies completely invalid number returns False
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("123456789012"))

    def test26(self):
        """Verifies valid Visa is accepted independently
        Picked using Partition Testing"""
        self.assertTrue(credit_card_validator("4000000000000002"))

    def test27(self):
        """Verifies 2221 prefix with invalid check digit
        Picked using Partition Testing"""
        self.assertFalse(credit_card_validator("2221000000000008"))

    def test28(self):
        """Verifies 2720 prefix with invalid check digit
        Picked using Partition Testing"""
        self.assertFalse(credit_card_validator("2720000000000004"))

    def test29(self):
        """Verifies AmEx 37 invalid check digit
        Picked using Partition Testing"""
        self.assertFalse(credit_card_validator("370000000000003"))

    def test30(self):
        """Verifies invalid 3-series not AmEx
        Picked using Error Guessing"""
        self.assertFalse(credit_card_validator("360000000000008"))

    def test31(self):
        """Verifies Visa with valid prefix/length and different invalid check digit returns False
        Picked using Partition Testing to try another Visa checksum case"""
        self.assertFalse(credit_card_validator("4000000000000003"))

    def test32(self):
        """Verifies Visa with another valid number returns True
        Picked using Partition Testing to cover an additional valid Visa example"""
        self.assertTrue(credit_card_validator("4012888888881881"))

    def test33(self):
        """Verifies MasterCard prefix 52 is accepted
        Picked using Partition Testing for an interior value in the 51-55 range"""
        self.assertTrue(credit_card_validator("5200000000000007"))

    def test34(self):
        """Verifies MasterCard prefix 53 is accepted
        Picked using Partition Testing for an interior value in the 51-55 range"""
        self.assertTrue(credit_card_validator("5300000000000006"))

    def test35(self):
        """Verifies MasterCard prefix 54 is accepted
        Picked using Partition Testing for an interior value in the 51-55 range"""
        self.assertTrue(credit_card_validator("5400000000000005"))

    def test36(self):
        """Verifies MasterCard prefix 52 with invalid check digit returns False
        Picked using Partition Testing by changing only the checksum"""
        self.assertFalse(credit_card_validator("5200000000000008"))

    def test37(self):
        """Verifies MasterCard prefix 2222 is accepted
        Picked using Boundary Value Testing just above the lower 4-digit boundary"""
        self.assertTrue(credit_card_validator("2222000000000008"))

    def test38(self):
        """Verifies MasterCard prefix 2719 is accepted
        Picked using Boundary Value Testing just below the upper 4-digit boundary"""
        self.assertTrue(credit_card_validator("2719000000000002"))

    def test39(self):
        """Verifies prefix 2721 with valid length and check digit returns False
        Picked using Boundary Value Testing to isolate the prefix error"""
        self.assertFalse(credit_card_validator("2721000000000004"))

    def test40(self):
        """Verifies prefix 2220 with valid length and check digit returns False
        Picked using Boundary Value Testing to isolate the prefix error"""
        self.assertFalse(credit_card_validator("2220000000000000"))


if __name__ == '__main__':
    unittest.main()