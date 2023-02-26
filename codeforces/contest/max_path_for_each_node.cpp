#include <bits/stdc++.h>
 
using namespace std;
 
vector<int> g[200010];
int d1[200010], d2[200010];
 
void dfs1(int i = 0, int p = -1, int d = 0) {
  d1[i] = d;
  for(auto j : g[i])
    if(j != p)
      dfs1(j, i, d + 1);
}
 
void dfs2(int i = 0, int p = -1, int d = 0) {
  d2[i] = d;
  for(auto j : g[i])
    if(j != p)
      dfs2(j, i, d + 1);
}
 
int main() {
  int n;
  cin >> n;
  for(int i = 1; i < n; i++) {
    int a, b;
    cin >> a >> b;
    g[a - 1].push_back(b - 1);
    g[b - 1].push_back(a - 1);
  }
  dfs1();
  dfs2(max_element(d1, d1 + n) - d1);
  dfs1(max_element(d2, d2 + n) - d2);
  for(int i = 0; i < n; i++) {
    cout << max(d1[i], d2[i]) << ' ';
  }
  cout << '\n';
}