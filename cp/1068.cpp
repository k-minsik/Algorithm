#include <bits/stdc++.h>
using namespace std;

int n, d, root, temp;
vector<int> t[51];

int dfs(int cur) {
    int leaf = 0;
    int child = 0;

    for(auto i : t[cur]) {
        if(i != d) {
            leaf += dfs(i);
            child++;
        }
    }
    
    if(child == 0) return 1;

    return leaf;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> temp;
        if (temp == -1) {
            root = i;
        }
        else{
            t[temp].push_back(i);
        }
    }

    cin >> d;

    if(d == root) {
        cout << 0 << "\n";
        return 0;
    }

    cout << dfs(root) << "\n";

    return 0;
}