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