class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        if '0' not in binary:
            return binary
        counter = Counter(binary)
        count = 0
        for char in binary:
            if char == '1':
                count += 1
            else:
                break
        return "1"*(count + counter['0'] - 1) + "0" + '1' * (counter['1'] - count)
    