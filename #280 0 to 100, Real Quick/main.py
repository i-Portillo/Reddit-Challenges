
def validate(hand):
    lHand, rHand = hand[:len(hand) // 2], hand[len(hand) // 2:]

    valid = True
    found = False

    for i in range(len(lHand)-1):
        if lHand[i] == '0':
            if found is True:
                print("Invalid")
                valid = False
                break
            else:
                continue
        if lHand[i] == '1':
            if found is False:
                found = True
            continue

    found = False
    for i in range(len(rHand)-1):
        if rHand[i+1] == '1':
            if found is True:
                print("Invalid")
                valid = False
                break
            else:
                continue
        if rHand[i+1] == '0':
            if found is False:
                found = True
            continue

    return valid


def get_value(hand):

    finger_values = [10, 10, 10, 10, 50, 5, 1, 1, 1, 1]
    value = 0

    for i in range(len(hand)):
        value += int(hand[i]) * finger_values[i]

    return value

hand = "0111101100"

if validate(hand):
    print(get_value(hand))
