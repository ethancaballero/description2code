'''
Created on 21-Jul-2015

@author: Venkatesh
'''


def read_int_list():
    return [int(x) for x in raw_input().split()]


def read_int():
    return int(raw_input())


def get_max_sum(nums, n, d):
    nums.sort(reverse=True)
    total, ind = 0, 0
    while ind+1 < n:
        diff = nums[ind] - nums[ind+1]
        if diff < d:
            total += nums[ind] + nums[ind+1]
            ind += 1
        ind += 1
    return total


def main():
    tc = read_int()
    for _ in xrange(tc):
        n, d = read_int_list()
        nums = read_int_list()
        print get_max_sum(nums, n, d)


if __name__ == '__main__':
    main()
