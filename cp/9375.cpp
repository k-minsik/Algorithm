#include <bits/stdc++.h>
using namespace std;

int tc, n;
string name, what;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> tc;

    for(int i = 0; i < tc; i++) {
        map<string, int> bag;
        cin >> n;
        for(int j = 0; j < n; j++) {
            cin >> name >> what;
            bag[what]++;

        }
        int res = 1;
        for(auto i : bag) res *= ((int)i.second + 1);
        cout << res - 1 << "\n";
    }

    return 0;
}