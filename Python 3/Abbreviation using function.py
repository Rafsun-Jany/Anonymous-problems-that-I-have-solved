def abbreviation(string1, string2):
    string2 = list(string2)
    temp = []
    temp = temp + list(string1[0])
    for i in range(0, len(string1)):
        if string1[i] == " ":
            temp = temp + list(string1[i + 1])
    if temp == string2:
        print("Yes, Correct Abbreviation")
    else:
        print("No, Not Correct Abbreviation")


if __name__ == "__main__":
    string1 = "Bangladesh Bank"
    string2 = "BB"
    abbreviation(string1,string2)
