import sys


def main():
    phone = input('휴대 전화 번호 입력 (ex: 010-9911-6611):')
    comm = check_command(phone)
    print(f'당신은 {comm}사용자 입니다.')
def check_command(n):

    pnum = n.split('-')[0]
    if pnum == '011':
        ret = 'skt'
    elif pnum == '016':
        ret = 'kt'
    elif pnum == '019':
        ret = 'lg'
    else:
        sys.exit()

    return ret

if __name__ == "__main__":
    main()