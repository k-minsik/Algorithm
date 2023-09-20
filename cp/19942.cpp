#include <bits/stdc++.h>
using namespace std;

int n, mp, mf, ms, mv, ret = 1e9;
int sp, sf, ss, sv, sc;
map<int, vector<vector<int>>> answer;

struct food{
    int p, f, s, v, c;
}arr[16];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);


    cin >> n;
    cin >> mp >> mf >> ms >> mv;

    for (int i = 0; i < n; i++) {
        cin >> arr[i].p >> arr[i].f >> arr[i].s >> arr[i].v >> arr[i].c;
    }

    for (int i = 1; i < (1 << n); i++) {
        sp = sf = ss = sv = sc = 0;
        vector<int> temp;

        for (int j = 0; j < n; j++) {
            if (i & (1 << j)) {
                temp.push_back(j + 1);
                sp += arr[j].p;
                sf += arr[j].f;
                ss += arr[j].s;
                sv += arr[j].v;
                sc += arr[j].c;
            }
        }

        if (mp <= sp && mf <= sf && ms <= ss && mv <= sv) {
            if (sc <= ret) {
                ret = sc;
                answer[ret].push_back(temp);
            }
        }
    }

    if (ret == 1e9) cout << -1 << "\n";
    else {
        cout << ret << "\n";
        sort(answer[ret].begin(), answer[ret].end());
        for (auto i : answer[ret][0]) cout << i << " ";
    }

    return 0;
}