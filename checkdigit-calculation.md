### TMS Check Digit Calculation Steps

To calculate the TMS check digit, follow these steps:

1. **Pad TMS Number**: Pad the TMS number with zeros to make it 6 characters long, while preserving the leading letters.
2. **Convert Characters to Digits**: Convert each character in the padded TMS number to digits using the following rules:
   * For letters (A-Z), subtract 64 from the ASCII value to get a value between 1 and 26 (A = 1, Z = 26).
3. **Calculate Weighted Sum**: Calculate the weighted sum of the digits by multiplying each digit by 2 raised to the power of its index (starting from index 0).
4. **Calculate Check Digit**: Calculate the check digit by taking the remainder of the weighted sum when divided by 11.

### Example Calculation

Let's calculate the TMS check digit for the number "DSA483".

1. **Pad TMS Number**: Pad the TMS number with zeros to make it 6 characters long: "DSA048".
   * We now have [D, S, A, 0, 4, 8]
2. **Convert Characters to Digits**:
   * "D" becomes [0, 4] (since ASCII value of "D" is 68, and 68 - 64 = 4)
   * "S" becomes [1, 9] (since ASCII value of "S" is 83, and 83 - 64 = 19)
   * "A" becomes [0, 1] (since ASCII value of "A" is 65, and 65 - 64 = 1)
   * We now have: [0, 4, 1, 9, 0, 1, 0, 4, 8]
3. **Calculate Weighted Sum**:
   * 0 x 2^0 = 0
   * 4 x 2^1 = 8
   * 1 x 2^2 = 4
   * 9 x 2^3 = 72
   * 0 x 2^4 = 0
   * 1 x 2^5 = 32
   * 0 x 2^6 = 0
   * 4 x 2^7 = 512
   * 8 x 2^8 = 2048
   * Total = 0 + 8 + 4 + 72 + 0 + 32 + 0 + 512 + 2048 = 2676
4. **Calculate Check Digit**: Calculate the check digit:
   * Check digit = 2676 % 11 = 3
