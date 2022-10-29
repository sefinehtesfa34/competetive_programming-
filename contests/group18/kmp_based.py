def get_string():
    return input()
    
def main():
    
    string = get_string()
    prefix = [0]*(len(string))
    left = 0
    right = 1
    while right < len(string):
        if string[left] == string[right]:
            prefix[right] = left + 1
            left += 1
            right += 1
        elif left > 0:
            left = prefix[left - 1]
        else:
            right += 1
    length = prefix[-1]
    if length  < len(string) // 3:
        substr = string[:length]
        if substr in string[length:-length]:
            print(substr)
        else:
            print("Just a legend")
    else:
        pass 
        
main()
            
                
                
                
            
    