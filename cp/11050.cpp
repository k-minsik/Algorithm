#include <bits/stdc++.h>
using namespace std;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    int n, k, ret;
    cin >> n >> k;

    k = min(k, n-k);
    ret = 1;

    for(int i = 0; i < k; i++){
        ret *= n - i; 
    }
    for(int i = 0; i < k; i++){
        ret /= k - i; 
    }

    cout << ret << "\n";

    return 0;
}