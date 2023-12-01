#!/usr/bin/python
# Modules
import random

# Global Variables

# Functions
def lotto_num_choice(nums):
    # input: list(nums)
    # output: list(6 numbers)
    # function: (lists -> shuffle -> choice)*6 => (6 numbers)
    ret = []
    for i in range(6):
        random.shuffle(nums)
        choice = nums.pop()
        ret.append(choice)
    return ret

def prt_lotto(nums):
    # input: list(6 numbers) => [12, 13, 14, 15, 16, 17]
    # output: str(6 numbers) => 12 13 14 15 16 17
    # function:
    for i in nums:
        print(i, end=' ')

def main():
    # 1) 로또 번호 생성 : 1,2,3,4,...,45
    lotto_num_list = [i for i in range(1, 46)]
    # 2) 로또 번호 선정 : 6개 무작위 추출
    lotto_choice = lotto_num_choice(lotto_num_list)
    # 3) 출력
    prt_lotto(lotto_choice)

if __name__ == '__main__':
    results = map(lambda x: (x * x), [0, 1, 2, 3])
    print(list(results))
    print(__name__)
    main()

