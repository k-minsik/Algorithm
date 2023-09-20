#include <bits/stdc++.h>
using namespace std;

int n, m, a, b, arr[101];

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> m;

    for(int i = 1; i <= n; i++) {
        arr[i] = i;
    }
    for(int i = 0; i < m; i++) {
        cin >> a >> b;
        while (b > a) {
            int temp = arr[a];
            arr[a] = arr[b];
            arr[b] = temp;
            a++; b--;
        }

    }

    for(int i = 1; i <= n; i++) {
        cout << arr[i] << " ";
    }


    return 0;
}