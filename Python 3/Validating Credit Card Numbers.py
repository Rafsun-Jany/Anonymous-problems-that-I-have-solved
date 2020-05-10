"""
You and Fredrick are good friends. Yesterday, Fredrick received  credit cards from ABCD Bank. He wants to verify whether his credit card numbers are valid or not. You happen to be great at regex so he is asking for your help!

A valid credit card from ABCD Bank has the following characteristics:

► It must start with a 4,5,6  or .
► It must contain exactly  16 digits.
► It must only consist of digits (0-9).
► It may have digits in groups of ,4 separated by one hyphen "-".
► It must NOT use any other separator like ' ' , '_', etc.
► It must NOT have 4 or more consecutive repeated digits.
"""
import re


def valid_or_not():
    credit_cards_number = int(input())
    if 0 < credit_cards_number < 100:
        for iterator in range(credit_cards_number):
            card_number = input()
            if len(card_number) == 16 or len(card_number) == 19:
                match = re.search(r'[456]\d{3}\-?\d{4}\-?\d{4}\-?\d{4}', card_number)
                if match and consecutive_digits(card_number) < 4:
                    print("Valid")
                else:
                    print("Invalid")
            else:
                print("Invalid")


def consecutive_digits(card_number):
    k = 0
    card_number = list(card_number.replace("-", ""))
    for i in range(len(card_number) - 2):
        count = 1
        for j in range(i + 1, len(card_number) - 1):
            if card_number[i] == card_number[j]:
                count += 1
            else:
                break
        if count > k:
            k = count
    return k


if __name__ == "__main__":
    valid_or_not()
