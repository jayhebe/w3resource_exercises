def number_of_notes(amount, notes):
    result = 0
    for note in list(reversed(notes)):
        if amount // note != 0:
            result += (amount // note)
            amount = amount % note

    return result


note_list = [10, 20, 50, 100, 200, 500]

print(number_of_notes(880, note_list))
print(number_of_notes(1000, note_list))
