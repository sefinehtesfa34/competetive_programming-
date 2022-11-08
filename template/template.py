from heapq import * 
from collections import *
from math import *
from itertools import accumulate
from string import ascii_lowercase,ascii_uppercase
def get_int():
    return int(input())
def get_nums():
    return list(map(int, input().split()))
def get_str():
    return input()
def main():
    n, x = get_nums()
    nums = get_nums()
    counter = Counter(nums)
    nums = sorted(set(nums))
    max_val = nums[0]
    
    for num in nums[:-1]:
        count = counter[num]
        if count % (num + 1) == 0:
            counter[num + 1] += count // (num  + 1)
            max_val = max(max_val, num + 1)
    heap = [(max_val, counter[max_val])]
    heapify(heap)
    
    while heap:
        val, count = heappop(heap)
        if val % x == 0:
            return print("YES")
        if count % (val + 1) != 0:
            return print("NO")
        heappush(heap, (val + 1, count // (val + 1)))
main()    
# 483363 644
# 524 112 133 355 600 363 287 644 627 378 532 394 552 58 499 303 463 402 178 179 361 532 644 589 532 312 461 644 519 435 409 275 618 125 268 374 569 498 430 153 644 633 596 644 644 462 606 519 468 625 362 506 468 213 597 372 442 533 606 452 382 428 644 274 443 414 644 511 471 250 548 377 644 459 453 168 548 644 377 644 348 553 491 545 432 594 631 529 591 187 517 583 545 549 605 367 486 281 301 526 315 323 599 340 311 549 308 585 472 204 630 449 644 600 562 261 542 212 118 456 538 404 611 147 622
