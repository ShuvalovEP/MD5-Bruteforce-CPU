from itertools import product
from hashlib import md5
import datetime

# md5_hash = '202cb962ac59075b964b07152d234b70' #123
# md5_hash = '81dc9bdb52d04dc20036dbd8313ed055' #1234
# md5_hash = '827ccb0eea8a706c4c34a16891f84e7b' #12345
# md5_hash = 'e10adc3949ba59abbe56e057f20f883e' #123456
# md5_hash = 'fcea920f7412b5da7be0cf42b8c93759' #1234567
# md5_hash = '25d55ad283aa400af464c76d713c07ad' #12345678
# md5_hash = '25f9e794323b453885f5181f1b624d0b' #123456789
# md5_hash = 'e807f1fcf82d132f9bb018ca6738a19f' #1234567890


ascii_ranges = []


for i in range(33, 126):
    ascii_ranges.append(chr(i))


def bruteforce(input_md5):
    pass_try = 0
    for iteration in range(1, 63 + 1):  # Длинна пароля
        start = datetime.datetime.now()
        print(iteration)
        for item in product(ascii_ranges, repeat=iteration):
            item_string = ''.join(item)
            pass_try += 1
            if md5(item_string.encode('utf-8')).hexdigest() == input_md5:
                delta = datetime.datetime.now() - start
                try:
                    spead = pass_try // delta.seconds
                except ZeroDivisionError:
                    spead = pass_try
                print(
                    '\n    - Password:', item_string,
                    '\n    - Length:', iteration, 'symbol',
                    '\n    - Time:', delta.seconds, 'sec',
                    '\n    - Spead:', spead, 'pass/sec'
                    '\n    - Generated:', pass_try, 'pass'
                    '\n    - Hash MD5:', input_md5
                )
                exit()


def main():
    input_md5 = input('Enter hash to crack: ')
    return bruteforce(input_md5)


if __name__ == '__main__':
    main()
