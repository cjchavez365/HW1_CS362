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
        """Verifies MasterCard prefix 2719 is accepted
        Picked using Category Partition Testing for an interior valid value
        in the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2719000000000008"))

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

    def test39(self):
        """Verifies MasterCard prefix 2230 is accepted
        Picked using Category Partition Testing for another interior valid
        value in the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2230000000000008"))

    def test40(self):
        """Verifies MasterCard prefix 2230 with invalid check digit returns False
        Picked using Category Partition Testing by changing only the checksum"""
        self.assertFalse(credit_card_validator("2230000000000009"))

    def test41(self):
        """Verifies AmEx prefix 35 is rejected
        Picked using Partition Testing to check another invalid 3x prefix"""
        self.assertFalse(credit_card_validator("350000000000006"))

    def test43(self):
        """Verifies prefix 36 is rejected with valid length and valid checksum
        Picked using Category Partition Testing to isolate invalid prefix only"""
        self.assertFalse(credit_card_validator("360000000000004"))

    def test44(self):
        """Verifies AmEx prefix 37 with length 14 returns False
        Picked using Boundary Value Testing just below valid AmEx length"""
        self.assertFalse(credit_card_validator("37000000000000"))

    def test45(self):
        """Verifies AmEx prefix 37 with length 16 returns False
        Picked using Boundary Value Testing just above valid AmEx length"""
        self.assertFalse(credit_card_validator("3700000000000000"))

    def test46(self):
        """Verifies another Visa with valid prefix and invalid check digit returns False
        Picked using Partition Testing to try a different Visa checksum case"""
        self.assertFalse(credit_card_validator("4012888888881882"))

    def test47(self):
        """Verifies MasterCard prefix 2222 with invalid check digit returns False
        Picked using Partition Testing on an interior 2221-2720 value"""
        self.assertFalse(credit_card_validator("2222000000000009"))

    def test48(self):
        """Verifies MasterCard prefix 2719 with invalid check digit returns False
        Picked using Partition Testing on an interior upper-range value"""
        self.assertFalse(credit_card_validator("2719000000000003"))

    def test49(self):
        """Verifies MasterCard prefix 2223 is accepted
        Picked using Category Partition Testing for an interior valid value
        in the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2223000048400011"))

    def test50(self):
        """Verifies MasterCard prefix 2701 is accepted
        Picked using Category Partition Testing for another interior valid value
        in the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2701000000000008"))

    def test51(self):
        """Verifies MasterCard prefix 2223 with invalid check digit returns False
        Picked using Category Partition Testing by changing only the checksum"""
        self.assertFalse(credit_card_validator("2223000000000008"))

    def test52(self):
        """Verifies MasterCard prefix 2701 with invalid check digit returns False
        Picked using Category Partition Testing by changing only the checksum"""
        self.assertFalse(credit_card_validator("2701000000000009"))

    def test53(self):
        """Verifies American Express prefix 34 with a different valid card returns True
        Picked using Category Partition Testing for another valid AmEx-34 frame"""
        self.assertTrue(credit_card_validator("341234567890123"))

    def test54(self):
        """Verifies American Express prefix 34 with invalid check digit returns False
        Picked using Category Partition Testing by changing only the checksum"""
        self.assertFalse(credit_card_validator("341111111111112"))

    def test55(self):
        """Verifies American Express prefix 37 with a different valid card returns True
        Picked using Category Partition Testing for another valid AmEx-37 frame"""
        self.assertTrue(credit_card_validator("378282246310005"))

    def test56(self):
        """Verifies American Express prefix 37 with invalid check digit returns False
        Picked using Category Partition Testing by changing only the checksum"""
        self.assertFalse(credit_card_validator("378282246310006"))

    def test57(self):
        """Verifies Visa with a different valid nonzero body returns True
        Picked using Category Partition Testing for another valid Visa frame"""
        self.assertTrue(credit_card_validator("4123456789012349"))

    def test58(self):
        """Verifies MasterCard prefix 51 with a different valid nonzero body returns True
        Picked using Category Partition Testing for another valid 51-55 frame"""
        self.assertTrue(credit_card_validator("5112345678901235"))

    def test59(self):
        """Verifies MasterCard prefix 2221 with a different valid nonzero body returns True
        Picked using Category Partition Testing for another valid 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2221123456789014"))

    def test60(self):
        """Verifies MasterCard prefix 2701 with a different valid nonzero body returns True
        Picked using Category Partition Testing for another valid 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2701123456789013"))

    def test61(self):
        """Verifies American Express prefix 34 with a different valid nonzero body returns True
        Picked using Category Partition Testing for another valid AmEx-34 frame"""
        self.assertTrue(credit_card_validator("341234567890127"))

    def test62(self):
        """Verifies American Express prefix 37 with a different valid nonzero body returns True
        Picked using Category Partition Testing for another valid AmEx-37 frame"""
        self.assertTrue(credit_card_validator("371234567890120"))

    def test63(self):
        """Verifies Visa with a different valid body returns True
        Picked using Category Partition Testing for another valid Visa frame"""
        self.assertTrue(credit_card_validator("4556737586899855"))

    def test64(self):
        """Verifies Visa with another valid body returns True
        Picked using Category Partition Testing for a nontrivial valid Visa frame"""
        self.assertTrue(credit_card_validator("4532015112830366"))

    def test65(self):
        """Verifies MasterCard prefix 51 with a different valid body returns True
        Picked using Category Partition Testing for another valid 51-55 frame"""
        self.assertTrue(credit_card_validator("5105105105105100"))

    def test66(self):
        """Verifies MasterCard prefix 55 with a different valid body returns True
        Picked using Category Partition Testing for another valid 51-55 frame"""
        self.assertTrue(credit_card_validator("5555555555554444"))

    def test67(self):
        """Verifies American Express prefix 34 with a different valid body returns True
        Picked using Category Partition Testing for another valid AmEx-34 frame"""
        self.assertTrue(credit_card_validator("349876543210123"))

    def test68(self):
        """Verifies American Express prefix 37 with a different valid body returns True
        Picked using Category Partition Testing for another valid AmEx-37 frame"""
        self.assertTrue(credit_card_validator("371449635398431"))

    def test69(self):
        """Verifies MasterCard prefix 53 with a nonzero valid body returns True
        Picked using Category Partition Testing for an interior 51-55 frame"""
        self.assertTrue(credit_card_validator("5312345678901233"))

    def test70(self):
        """Verifies MasterCard prefix 55 with a nonzero valid body returns True
        Picked using Category Partition Testing for an upper-bound 51-55 frame"""
        self.assertTrue(credit_card_validator("5512345678901231"))

    def test71(self):
        """Verifies MasterCard prefix 2229 with a nonzero valid body returns True
        Picked using Category Partition Testing for an early interior 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2229123456789016"))

    def test72(self):
        """Verifies MasterCard prefix 2231 with a nonzero valid body returns True
        Picked using Category Partition Testing for another interior 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2231123456789012"))

    def test73(self):
        """Verifies MasterCard prefix 2600 with a nonzero valid body returns True
        Picked using Category Partition Testing for a middle 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2600123456789015"))

    def test74(self):
        """Verifies MasterCard prefix 2699 with a nonzero valid body returns True
        Picked using Category Partition Testing for an upper interior 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2699123456789017"))

    def test75(self):
        """Verifies MasterCard prefix 2710 with a nonzero valid body returns True
        Picked using Category Partition Testing for a late 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2710123456789012"))

    def test76(self):
        """Verifies MasterCard prefix 2718 with a nonzero valid body returns True
        Picked using Category Partition Testing for a late interior 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2718123456789014"))

    def test77(self):
        """Verifies MasterCard prefix 2720 with a nonzero valid body returns True
        Picked using Category Partition Testing for the upper boundary with a realistic body"""
        self.assertTrue(credit_card_validator("2720123456789010"))

    def test78(self):
        """Verifies MasterCard prefix 2229 is accepted
        Picked using Boundary Value Testing at an internal transition point
        in the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2229000000000001"))

    def test79(self):
        """Verifies MasterCard prefix 2299 is accepted
        Picked using Boundary Value Testing at an internal transition point
        in the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2299000000000006"))

    def test80(self):
        """Verifies MasterCard prefix 2300 is accepted
        Picked using Boundary Value Testing at an internal transition point
        in the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2300000000000003"))

    def test81(self):
        """Verifies MasterCard prefix 2699 is accepted
        Picked using Boundary Value Testing at an internal transition point
        in the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2699000000000002"))

    def test82(self):
        """Verifies MasterCard prefix 2700 is accepted
        Picked using Boundary Value Testing at an internal transition point
        in the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2700000000000009"))

    def test83(self):
        """Verifies MasterCard prefix 2710 is accepted
        Picked using Boundary Value Testing at an internal transition point
        in the 2221-2720 range"""
        self.assertTrue(credit_card_validator("2710000000000007"))

    def test84(self):
        """Verifies MasterCard prefix 2718 is accepted
        Picked using Boundary Value Testing just below an already tested
        valid prefix near the top of the range"""
        self.assertTrue(credit_card_validator("2718000000000009"))

    def test85(self):
        """Verifies invalid prefix with valid checksum returns False
        Picked using Category Partition Testing to isolate prefix only"""
        self.assertFalse(credit_card_validator("6011111111111117"))

    def test86(self):
        """Verifies invalid prefix with valid checksum returns False
        Picked using Category Partition Testing to isolate prefix only"""
        self.assertFalse(credit_card_validator("9111111111111116"))

    def test87(self):
        """Verifies valid Visa checksum but invalid length returns False
        Picked using Category Partition Testing to isolate length only"""
        self.assertFalse(credit_card_validator("411111111111111"))  # 15 digits

    def test88(self):
        """Verifies valid Visa checksum but invalid length returns False
        Picked using Category Partition Testing to isolate length only"""
        self.assertFalse(credit_card_validator("41111111111111111"))  # 17 digits

    def test89(self):
        """Verifies valid AmEx checksum but invalid prefix returns False
        Picked using Category Partition Testing to isolate prefix only"""
        self.assertFalse(credit_card_validator("351234567890123"))

    def test90(self):
        """Verifies valid AmEx checksum but invalid prefix returns False
        Picked using Category Partition Testing to isolate prefix only"""
        self.assertFalse(credit_card_validator("361234567890124"))

    def test91(self):
        """Verifies MasterCard prefix 52 with a nonzero valid body returns True
        Picked using Category Partition Testing for another valid 51-55 frame"""
        self.assertTrue(credit_card_validator("5212345678901232"))

    def test92(self):
        """Verifies MasterCard prefix 54 with a nonzero valid body returns True
        Picked using Category Partition Testing for another valid 51-55 frame"""
        self.assertTrue(credit_card_validator("5412345678901230"))

    def test93(self):
        """Verifies MasterCard prefix 2400 with a valid body returns True
        Picked using Category Partition Testing for an untested interior 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2400123456789012"))

    def test94(self):
        """Verifies MasterCard prefix 2500 with a valid body returns True
        Picked using Category Partition Testing for an untested interior 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2500123456789011"))

    def test95(self):
        """Verifies MasterCard prefix 2224 with a valid body returns True
        Picked using Category Partition Testing for an early interior 2221-2720 frame"""
        self.assertTrue(credit_card_validator("2224123456789019"))

    def test96(self):
        """Verifies MasterCard prefix 2720 with a different nonzero valid body returns True
        Picked using Category Partition Testing for a second upper-bound valid frame"""
        self.assertTrue(credit_card_validator("2720992712345673"))

    def test98(self):
        """Invalid prefix but valid length and checksum (MC-style)
        Picked using Category Partition Testing to isolate prefix only"""
        self.assertFalse(credit_card_validator("6011000000000004"))

    def test99(self):
        """Invalid prefix but valid length and checksum (AmEx-style)
        Picked using Category Partition Testing to isolate prefix only"""
        self.assertFalse(credit_card_validator("351111111111118"))

    def test100(self):
        """Invalid prefix but valid length and checksum (AmEx-style)
        Picked using Category Partition Testing to isolate prefix only"""
        self.assertFalse(credit_card_validator("361111111111117"))

    def test101(self):
        """Valid Visa-like number with leading zero should be rejected
        Picked using Error Guessing for string parsing issues"""
        self.assertFalse(credit_card_validator("0411111111111111"))

    def test102(self):
        """Valid MasterCard-like number with leading zero should be rejected
        Picked using Error Guessing for string parsing issues"""
        self.assertFalse(credit_card_validator("0510000000000008"))

    def test103(self):
        """Valid AmEx-like number with leading zero should be rejected
        Picked using Error Guessing for string parsing issues"""
        self.assertFalse(credit_card_validator("034000000000009"))

    def test104(self):
        """Valid-length number with leading zero and valid checksum should be rejected
        Picked using Error Guessing for numeric parsing bugs"""
        self.assertFalse(credit_card_validator("0123456789012349"))

    def test105(self):
        """Valid Visa with check digit 0 should return True
        Picked using Boundary Value Testing for checksum edge case"""
        self.assertTrue(credit_card_validator("4000000000000000"))

    def test106(self):
        """Valid MasterCard with check digit 0 should return True
        Picked using Boundary Value Testing for checksum edge case"""
        self.assertTrue(credit_card_validator("5105105105105100"))

    def test107(self):
        """Valid MasterCard (2221 range) with check digit 0 should return True
        Picked using Boundary Value Testing for checksum edge case"""
        self.assertTrue(credit_card_validator("2223000048400010"))

    def test108(self):
        """Valid AmEx with check digit 0 should return True
        Picked using Boundary Value Testing for checksum edge case"""
        self.assertTrue(credit_card_validator("340000000000000"))

    def test109(self):
        """Valid Visa with minimal repeating pattern should return True
        Picked using Error Guessing for digit-pattern bugs"""
        self.assertTrue(credit_card_validator("4444444444444448"))

    def test110(self):
        """Valid MasterCard with minimal repeating pattern should return True
        Picked using Error Guessing for digit-pattern bugs"""
        self.assertTrue(credit_card_validator("5555555555554444"))

    def test111(self):
        """Valid MasterCard (2221 range) with repeating pattern should return True
        Picked using Error Guessing for digit-pattern bugs"""
        self.assertTrue(credit_card_validator("2222222222222220"))

    def test112(self):
        """Valid AmEx with repeating pattern should return True
        Picked using Error Guessing for digit-pattern bugs"""
        self.assertTrue(credit_card_validator("373737373737373"))

    def test113(self):
        """Verifies MasterCard prefix 2221 with valid checksum but length 15 returns False
        Picked using Category Partition Testing to isolate length only"""
        self.assertFalse(credit_card_validator("222100000000000"))

    def test114(self):
        """Verifies MasterCard prefix 2221 with valid checksum but length 17 returns False
        Picked using Category Partition Testing to isolate length only"""
        self.assertFalse(credit_card_validator("22210000000000000"))

    def test115(self):
        """Verifies American Express prefix 37 with valid checksum but length 14 returns False
        Picked using Category Partition Testing to isolate length only"""
        self.assertFalse(credit_card_validator("37000000000007"))

    def test116(self):
        """Verifies American Express prefix 37 with valid checksum but length 16 returns False
        Picked using Category Partition Testing to isolate length only"""
        self.assertFalse(credit_card_validator("3700000000000007"))

    def test117(self):
        """Verifies invalid prefix 39 with valid checksum and AmEx length returns False
        Picked using Category Partition Testing to isolate prefix only"""
        self.assertFalse(credit_card_validator("390000000000001"))

    def test118(self):
        """Verifies invalid prefix 57 with valid checksum and MasterCard length returns False
        Picked using Category Partition Testing to isolate prefix only"""
        self.assertFalse(credit_card_validator("5700000000000007"))


if __name__ == '__main__':
    unittest.main()
