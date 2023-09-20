#include <bits/stdc++.h>
using namespace std;

int n, arr[16];
int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    arr[0] = 2;
    cin >> n;
    for(int i = 1; i < 16; i++) {
        arr[i] = 2 * arr[i-1] - 1;
    }

    cout << arr[n] * arr[n] << "\n";

    return 0;
}