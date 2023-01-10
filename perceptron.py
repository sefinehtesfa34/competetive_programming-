class Solution:
    def get_weights(self, x, y, w1, w2, output):
        early_stopping = 0.001
        lr = 0.01
        cur_output = w1*x + w2*y
        while abs(output - cur_output) > early_stopping:
            w1 += x*(output - cur_output)*lr
            w2 += y*(output - cur_output)*lr
            cur_output = w1*x + w2*y
        return w1, w2
     
solution = Solution()
def find_xor_weights():
    w1 = w2 = 0.5
    for _ in range(100):
        for x, y, output in [(1, 0, 1), (0, 1, 1), (1, 1, 0)]:
            w1, w2 = solution.get_weights(x, y, w1, w2, output)
    return w1, w2 
def find_and_weights():
    w1 = w2 = 0.5
    for _ in range(100):
        for x, y, output in [(1, 0, 0), (0, 1, 0), (1, 1, 1)]:
            w1, w2 = solution.get_weights(x, y, w1, w2, output)
    return w1, w2 
xor_w1, xor_w2 = find_xor_weights()
and_w1, and_w2 = find_and_weights()
x = 1
y = 1
predict_xor = x*xor_w1 + y*xor_w2 
predict_and = x*and_w1 + y*and_w2
print(predict_xor)
print(predict_and)

