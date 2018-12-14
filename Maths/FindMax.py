# NguyenU

def find_max(nums):
    max = nums[0]
    for y in nums:
      if y > max:
        max = y
    print(max)

def main():
  find_max([3, 7, 11, 19, 21, 91, 1])

if __name__ == '__main__':
  main()
