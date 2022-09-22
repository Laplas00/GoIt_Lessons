from curses import keyname


points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
}


def calculate_distance(coordinates):
    sum = 0
    nums = []
    while True:
        if len(coordinates) <= 1:
            False
            break
        print(coordinates)
        print("-------------")
        if len(nums) < 2:
            nums.append(coordinates[0])
            nums.append(coordinates[1])
            continue
        else:
            if nums[0] > nums[1]:
                print("==========")
                print("before ", nums)
                nums[0], nums[1] = nums[1], nums[0]
                print("after", nums)
                nums = tuple(nums)
                print(nums, "nums is not ok, but now ok")
            else:
                nums = tuple(nums)
                print(nums, "opa opa, all good")
        print(coordinates, "before coordinates")
        coordinates.pop(0)
        print(coordinates, "after coordinates")
        if nums in points:
            sum += points[nums]
            nums = []
        else:
            print('no direction for this keys ')
            nums = []
        print(f"sum is {sum}, and nums is {nums}")
        continue
    print(sum)
    return sum


calculate_distance([0, 1, 3, 2, 0, 2, ])
