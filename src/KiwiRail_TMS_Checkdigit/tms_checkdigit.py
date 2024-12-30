def convert_char_to_digits(char: str) -> list[int]:
    """
    Convert a character to a list of digits based on its ASCII value.

    ASCII is a way of representing characters as numbers. For example, the letter "A" has an ASCII value of 65.
    The ASCII number is indexed to 1, and zero padded e.g. "A" -> 65 -> 1 -> -> 01 -> [0, 1]
    """

    if char.isalpha():
        # Convert the letter to its uppercase ASCII value, and then subtract 64 to get a value between 1 and 26
        ascii_value = ord(char.upper()) - 64
        # Return a list with two digits: the tens digit and the ones digit
        return [ascii_value // 10, ascii_value % 10]

    elif char.isdigit():
        # If it's a digit, pass through the digit formatted as list with a single digit
        return [int(char)]

    else:
        raise ValueError(
            f"Invalid character {char}, only Letters or Numbers are allowed!"
        )


def raw_check_digit_calculation(tms_number: str) -> int:
    # Count the number of leading letters in the TMS number
    leading_letters = next(
        (i for i, char in enumerate(tms_number) if not char.isalpha()), len(tms_number)
    )

    # Pad the TMS number with zeros to make it 6 characters long
    # For example, "DSA48" becomes "DSA048" and "RM3" becomes "RM0003"
    padded_tms_number = tms_number[:leading_letters] + tms_number[
        leading_letters:
    ].zfill(6 - leading_letters)

    # Initialize the weighted sum
    weighted_sum = 0
    digit_index = 0

    # Convert each character in the padded TMS number to digits and calculate the weighted sum
    for char in padded_tms_number:
        for digit in convert_char_to_digits(char):
            # Calculate the weighted sum by multiplying each digit by 2 raised to the power of its index
            weighted_sum += digit * (2**digit_index)
            digit_index += 1

    # Calculate the check digit by taking the remainder of the weighted sum when divided by 11
    return weighted_sum % 11


def tms_number_format_valid(tms_number: str, length: int = 6) -> bool:
    return (
        len(tms_number) > 0
        and len(tms_number) <= length
        and tms_number[0].isalpha()
        and tms_number[-1].isdigit()
        and tms_number.isalnum()
    )


def calculate_check_digit(tms_number: str) -> int:
    """
    Calculate the check digit for a given TMS number.

    The check digit is a single digit at the end of a TMS number that is calculated based on the other digits in the TMS number.
    """

    # Validate the input TMS number
    if not tms_number_format_valid(tms_number):
        raise ValueError("Invalid TMS number")

    return raw_check_digit_calculation(tms_number)


def is_check_digit_valid(tms_number: str) -> bool:
    """
    Check if the check digit of a given TMS number is valid.

    The check digit is valid if it matches the calculated check digit for the given TMS number.
    """

    # Validate the input TMS number
    if not tms_number_format_valid(tms_number, 7):
        return False

    # Calculate the check digit for the given TMS number
    calculated_check_digit = raw_check_digit_calculation(tms_number[:-1])

    # Check if the calculated check digit matches the given check digit
    return calculated_check_digit == int(tms_number[-1])
