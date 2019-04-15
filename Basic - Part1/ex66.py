def get_bmi(weight_kg, height_meter):
    return weight_kg / height_meter ** 2


if __name__ == '__main__':
    print(get_bmi(70, 1.75))
