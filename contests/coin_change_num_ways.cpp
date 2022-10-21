count[0] = 1; //If the target is zero, we have got one possible path.
for (int x = 1; x <= n; x++) { // loops over all the target from bottom up.
    for (auto c : coins) { // loops over all the coins
        if (x-c >= 0) { // If the current coin is greater than the target, no need to count this path.
            count[x] += count[x-c]; // count the number of ways to reach the target sum
        }
    }
}
cout << count[x] <<endle;
