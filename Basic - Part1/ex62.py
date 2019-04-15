def convert_to_sec(hours, minutes, seconds):
    return hours * 3600 + minutes * 60 + seconds


if __name__ == '__main__':
    print(convert_to_sec(1, 20, 18))
