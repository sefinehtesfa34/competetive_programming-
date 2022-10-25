def get_test():
    return int(input())
def get_string():
    return input()


def main():
    string = get_string()
    test = get_test()
    for _ in range(test):
        curr_str =  get_string()
        prefix = [0]*(len(curr_str))
        left = 0
        right = 1
        while right < len(curr_str):
            if curr_str[left] == curr_str[right]:
                prefix[right] = left + 1
                left += 1
                right += 1
            elif left > 0:
                left = prefix[left - 1]
            else:
                right += 1
        str1 = 0
        str2 = 0
        while str1 < len(string):
            if string[str1] == curr_str[str2]:
                str1 += 1
                str2 += 1
            elif str2 > 0:
                str2 = prefix[str2 - 1]
            else:
                str1 += 1
            if str2 == len(curr_str):
                print("Yes")
                break
        else:
            print("No")
main()

        
        
        
        
        
        
        
        
        
        
        