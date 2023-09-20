#include <bits/stdc++.h>
using namespace std;

int n, m, s, e, temp, res;
int arr[15004];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    cin >> n;
    cin >> m;
    
    if(m > 200000) cout << 0  << "\n";
    else {
        for(int i = 0; i < n; i++) {
            cin >> temp;
            arr[i] = temp;
        }
        s = 0; e = n-1;
        sort(arr, arr + n);
        while(s < e) {
            if(arr[s] + arr[e] == m) {
                res += 1;
                s++;
                e--;
            }
            else if(arr[s] + arr[e] < m) {
                s++;
            }
            else e--;
        }
        cout << res << "\n";
    }

    return 0;
}