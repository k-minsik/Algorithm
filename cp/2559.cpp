#include <bits/stdc++.h>
using namespace std;

int n, k, temp, res = -987654321;
int psum[100004];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> k;

    for(int i = 1; i <= n; i++) {
        cin >> temp;
        psum[i] = psum[i-1] + temp;
    }

    for(int j = k; j <= n; j++) {
        res = max(res, psum[j] - psum[j-k]);

    }

    cout << res << "\n";

    return 0;
}