def getTest():
    return int(input())
def getNum():
    return int(input())
def main():
    test = getTest()
    for _ in range(test):
        num = getNum()
        nums = list(range(1, num + 1))
        left = 0
        right = len(nums) - 1
        answer = [] 
        turn = True 
        while left <= right:
            if turn:
                answer.append(nums[left])
                turn = False 
                left += 1
            else:
                answer.append(nums[right])
                turn = True 
                right -= 1
        for num in answer:
            print(num, end = ' ')
        print()
main()

        