'''
Diff Between Two Strings
Given two strings of uppercase letters source and target, list (in string form) 
a sequence of edits to convert from source to target that uses the least edits possible.
For example, with strings source = "ABCDEFG", and target = "ABDFFGH" we might return: 
["A", "B", "-C", "D", "-E", "F", "+F", "G", "+H"
More formally, for each character C in source, we will either write the token C, 
which does not count as an edit; or write the token -C, which counts as an edit.
Additionally, between any token that we write, we may write +D where D is any letter, 
which counts as an edit.
At the end, when reading the tokens from left to right, and not including tokens prefixed with a minus-sign, 
the letters should spell out target (when ignoring plus-signs.)
In the example, the answer of A B -C D -E F +F G +H has total number of edits 4 (the minimum possible), 
and ignoring subtraction-tokens, spells out A, B, D, F, +F, G, +H which represents the string target.
If there are multiple answers, use the answer that favors removing from the source first.

Constraints:

[time limit] 5000ms
[input] string source
2 ≤ source.length ≤ 12
[input] string target
2 ≤ target.length ≤ 12
[output] array.string
'''

def diffBetweenTwoStrings(source, target):
      # index for source
     # begin for target
      # temp: temporary array to store the current path
      # answer: the minimum possible edit path
      memo = {}
      def dp(index, begin, temp, counter):
            if (index, begin,counter) in memo:
                return memo[(index, begin, counter)]
            if index == len(source):
                  for cur in range(begin, len(target)):
                      temp.append("+" + target[cur])
                  return (counter + len(target) - begin, temp)
            if begin == len(target):
                  for cur in range(index, len(source)):
                      temp.append("-" + source[cur])
                  return (counter + len(source) - index, temp)
            if source[index] == target[begin]:
                  return  dp(index + 1, begin + 1, temp + [source[index]], counter)
            fromSource = dp(index + 1, begin, temp + ["-" + source[index]], counter + 1) 
            fromTarget = dp(index, begin + 1, temp + ["+" + target[begin]], counter + 1)
            if fromSource[0] == fromTarget[0]:
                memo[(index, begin,counter)] = fromSource
                return memo[(index, begin,counter)]
            memo[(index, begin,counter)] = min(fromSource, fromTarget)
            return memo[(index, begin, counter)]
      return dp(0, 0, [],0)[1]  
source = "ABCDEFG"
target = "ABDFFGH"
print(diffBetweenTwoStrings(source, target))