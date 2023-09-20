#include <bits/stdc++.h>
using namespace std;

int n, k, arr[51];

int count(int mask) {
    int cnt = 0;
    for (int c : arr) {
        if (c && (c & mask) == c) cnt++;
    }
    return cnt;
}

int go(int idx, int m, int mask) {
    if ( m < 0 ) return 0;
    if ( idx == 26 ) return count(mask);
    
    int answer = go(idx + 1, m - 1, mask | (1 << idx));
    if(idx != 'a'-'a' && idx != 'n'-'a' && idx != 't'-'a' && idx != 'i'-'a' && idx != 'c'-'a') {
        answer = max(answer, go(idx + 1, m, mask));
    }

    return answer;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> k;

    for(int i = 0; i < n; i++) {
        string s;
        cin >> s;
        for(char c : s) {
            arr[i] |= (1 << (c - 'a'));
        }
    }

    cout << go(0, k, 0) << "\n";

    return 0;
}