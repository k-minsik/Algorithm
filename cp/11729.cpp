#include <bits/stdc++.h>
using namespace std;

int n, cnt;
vector<pair<int, int>> ret;

void func(int a, int start, int end, int via) {
    cnt++;
    if (a == 1) {
        // cout << start << " " << end << "\n";
        ret.push_back({start, end});
        return;
    }

    func(a-1, start, via, end);
    // cout << start << " " << end << "\n";
    ret.push_back({start, end});
    func(a-1, via, end, start);

    return;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;
    if (n == 1) {
        cout << 1 << "\n";
        cout << 1 << " " << 3 << "\n";
        return 0;
    }

    func(n, 1, 3, 2);
    cout << cnt << "\n";
    for(auto i : ret) {
        cout << i.first << " " << i.second << "\n";
    }

    return 0;
}