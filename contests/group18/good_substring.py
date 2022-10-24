from string import ascii_lowercase
string = input()
good_bad = input()
k = int(input())
bad_strings = set()
for index in range(len(good_bad)):
    if good_bad[index] == '0':
        bad_strings.add(ascii_lowercase[index])
left = 0
right = 0
current_bad = 0
answer = set() 
while right < len(string):
    current_bad += int(string[right] in bad_strings)
    while current_bad > k:
        current_bad -= 1 if string[left] in bad_strings else 0
        left += 1
    temp = left 
    while temp <= right:
        answer.add(string[temp: right+ 1])
        temp += 1
    right += 1
    
print(len(answer))

    