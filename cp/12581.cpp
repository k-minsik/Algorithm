#include <bits/stdc++.h>
using namespace std;

int n, k, now;
int arr[200001], cnt[200001], visited[200001];
queue<int> q;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> n >> k;
    if(n == k) {
        cout << 0 << "\n";
        cout << 1 << "\n";
        return 0;
    }

    q.push(n);
    visited[n] = 1;
    cnt[n] = 1;

    while(q.size()) {
        now = q.front();
        q.pop();

        for(int next : {now-1, now+1, 2*now}) {
            if(next >= 0 && next <= 200000) {
                if(visited[next] == 0) {
                    q.push(next);
                    visited[next] = visited[now] + 1;
                    cnt[next] += cnt[now];
                }
                else if (visited[next] == visited[now] + 1) {
                    cnt[next] += cnt[now];
                }
            }
        }
    }

    cout << visited[k] - 1 << "\n";
    cout << cnt[k] << "\n";

    return 0;
}