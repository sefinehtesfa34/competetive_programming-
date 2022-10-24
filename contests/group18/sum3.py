
from typing import Counter


def main():
    test = int(input())
    for _ in range(test):
        
        n = int(input())
        nums = list(map(int, input().split()))
        modulos = []
        counter = Counter()
        for num in nums:
            modulo = num % 10
            if counter[modulo] <= 3:
                modulos.append(modulo)
            counter[modulo] += 1
        
        for index_i in range(len(modulos)):
            for index_j in range(index_i + 1, len(modulos)):
                for index_k in range(index_j + 1, len(modulos)):
                    current_sum =  modulos[index_i] + modulos[index_j] + modulos[index_k]
                    remainder = current_sum % 10
                    if remainder == 3:
                        print("YES")
                        # exit()
        print("NO") 
            
main()

import sys
import threading
sys.setrecursionlimit(1<<30)
threading.stack_size(1 << 27)
thread = threading.Thread(target=main)
thread.start()
thread.join()
# main()
