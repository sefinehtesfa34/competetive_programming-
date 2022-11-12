# def get_int():
#     return int(input())
# def get_nums():
#     return list(map(int, input().split()))
# def main():
#     test = get_int()
#     for _ in range(test):
#         n = int(input())
#         nums = get_nums()
#         nums.sort(reverse = True)
#         answer = []
#         for num in nums:
#             while num > n or (num // 2 not in answer and num//2 >= 1) :
#                 num //= 2
#             answer.append(num)
#         print(answer)
#         if len(set(answer)) == n:
#             print("YES")
#         else:
#             print("NO")
            
# main()