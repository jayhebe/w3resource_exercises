amount = "32.054,23"
maketrans = amount.maketrans
amount = amount.translate(maketrans(',.', '.,'))
print(amount)
