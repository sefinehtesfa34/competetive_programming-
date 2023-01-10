/*
x & (-x) : Returns the rightmost 1 in binary representation of x

(-x) is the two’s complement of x. (-x) will be equal to one’s complement of x plus 1.
Therefore (-x) will have all the bits flipped that are on the left of the rightmost 1 in x. 
So x & (-x) will return rightmost 1.

x = 10 = (1010)2
(-x) = -10 = (0110)2
x & (-x) = (1010)2 & (0110)2 = (0010)2

*/

class FenwickTree {
    private:
        vector<int> data;
    
        int getParent(int i) const {
            return i - (i & (-i));
        }
    
        int getNext(int i) const {
            return i + (i & (-i));
        }
    
    public:
        FenwickTree(int n) : data(n+1, 0) {
        }
    
        int getSum(int i) const {
            int sum = 0;
            ++i;
            while (i > 0) {
                sum += data[i];
                i = getParent(i);
            }
            return sum;
        }
    
        void update(int i, int v) {
            ++i;
            while (i < data.size()) {
                data[i] += v;
                i = getNext(i);
            }
        }
    };