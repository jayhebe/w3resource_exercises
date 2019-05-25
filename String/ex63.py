# def remove_zero_from_ip(ip_address):
#     result = []
#     segments = ip_address.split(".")
#     for seg in segments:
#         if seg != "0":
#             seg = seg.replace("0", "")
#         result.append(seg)
#
#     return ".".join(result)


def remove_zero_from_ip(ip_address):
    return ".".join([str(int(i)) for i in ip_address.split(".")])


if __name__ == '__main__':
    print(remove_zero_from_ip("255.024.01.01"))
    print(remove_zero_from_ip("127.0.0.01"))
