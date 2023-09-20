#include <bits/stdc++.h>
using namespace std;

int n, m, answer[10004], visited[10004], a, b, mx, res;
vector<int> arr[10004];

int dfs(int cur) {
    int cnt = 1;
    visited[cur] = 1;

    for(auto i : arr[cur]) {
        if(visited[i] == 0) {
            cnt += dfs(i);
        }
    }

    return cnt;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;
    for(int i = 0; i < m; i++){
        cin >> a >> b;
        arr[b].push_back(a);
    }

    for(int i = 1; i <= n; i++) {
        fill(&visited[0], &visited[0] + (n+1), 0);
        answer[i] = dfs(i);
        mx = max(answer[i], mx);

    }

    for(int i = 1; i <= n; i++) {
        if(answer[i] == mx) cout << i << " ";
    }

    return 0;
}