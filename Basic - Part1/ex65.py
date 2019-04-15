def convert_sec(seconds):
    days = seconds // (3600 * 24)
    hours = (seconds - days * (3600 * 24)) // 3600
    minutes = (seconds - hours * 3600) // 60
    seconds = (seconds - minutes * 60) % 60

    return days, hours, minutes, seconds


if __name__ == '__main__':
    d, h, m, s = convert_sec(60000)
    print("%d seconds is %d days, %d hours, %d minutes, %d seconds" % (1200, d, h, m, s))
