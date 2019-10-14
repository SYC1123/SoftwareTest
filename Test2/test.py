def testPhoneNumber(number):
    '''
    检查电话号正确性
    :param number: 电话号
    :return:
    '''
    number = str(number)
    if number.isdigit():
        if len(number) < 7 or 10 < len(number) or 7 < len(number) < 10:
            print('错误！（请输入正确的电话号码位数）')
        else:
            after = number[-4:]
            before = number[-7:-4]
            if before[0] == '0' or before[0] == '1':
                print('错误！（前缀码以"0"或”1”开头）')
            else:
                print('正确电话号码')
    else:
        print('错误！（请输入数字号码）')


if __name__ == '__main__':
    number = input('请输入电话号码')
    testPhoneNumber(number)
