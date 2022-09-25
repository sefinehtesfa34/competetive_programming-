'''
The "BerCorp" company has got n employees. These employees can use m approved official languages for the formal correspondence. 
The languages are numbered with integers from 1 to m. For each employee we have the list of languages, which he knows. 
This list could be empty, i. e. an employee may know no official languages. 
But the employees are willing to learn any number of official languages, as long as the company pays their lessons. 
A study course in one language for one employee costs 1 berdollar.
Find the minimum sum of money the company needs to spend so as any employee could correspond to 
any other one (their correspondence can be indirect, i. e. other employees can help out translating).

Input
The first line contains two integers n and m (2 ≤ n, m ≤ 100) — the number of employees and the number of languages.

Then n lines follow — each employee's language list. 
At the beginning of the i-th line is integer ki (0 ≤ ki ≤ m) 
— the number of languages the i-th employee knows. Next, the i-th line contains ki integers — aij (1 ≤ aij ≤ m) 
— the identifiers of languages the i-th employee knows. It is guaranteed that all the identifiers in one list are distinct. Note that an employee may know zero languages.

The numbers in the lines are separated by single spaces.

Output
Print a single integer — the minimum amount of money to pay 
so that in the end every employee could write a letter to every other one 
(other employees can help out translating).

'''
'''
8 7
1:0
2: 1 2 3
3: 1
4: 5 4
5: 6 7
6: 3
7: 7 4
8: 1
language:[employees]
 1:[2,8,3]
 2:[2]
 3:[2,6]
 4:[4,7]
 5:[4]
 6:[5]
 7:[5,7]
 
 2
 / \ \   4    1
8   3 6  / \
        7   5

'''
from collections import defaultdict
def find(person):
    if person == parent[person]:
        return person 
    parent[person] = find(parent[person])
    return parent[person] 

def union(person1, person2):
    parent1 = find(person1)
    parent2 = find(person2)
    if parent1 != parent2:
        parent[parent1] = parent2 
def build(languages, person, graph):
    
    for language in languages[1:]:
        graph[language].append(person)
N, M = list(map(int, input().split()))
graph = defaultdict(list)
parent = {}
zeros = 0
for person in range(1,N + 1):
    languages = list(map(int, input().split()))
    numLanguages = languages[0]
    if numLanguages != 0:
        build(languages, person, graph)
        parent[person] = person 
    else:
        zeros += 1
for language in graph:
    persons = graph[language]
    for index in range(len(persons) - 1):
        union(persons[index], persons[index + 1])

disconnectedComponents = set()
for person in range(1, N + 1):
    if person in parent:
        personParent = find(person)
        disconnectedComponents.add(personParent)
n = len(disconnectedComponents)
if n == 0:
    print(zeros)
    
else:
    print(n - 1 + zeros)
        
