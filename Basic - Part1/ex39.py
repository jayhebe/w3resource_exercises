def get_payback(spa, roi, years):
    """
    :param spa: Specified Principal Amount
    :param roi: Rate of Interest
    :param years: A number of years
    :return: Return on investment
    """
    return spa * pow(1 + roi / 100, years)


if __name__ == '__main__':
    print(get_payback(10000, 3.5, 7))
