#include <bits/stdc++.h>
using namespace std;

int n, l, a[101][101], b[101][101], answer;

int solve(int arr[101][101]) {
    int cnt = 0;

    for(int i = 0; i < n; i++) {
        int dist = 1;
        int j = 0;
        for(j = 0; j < n-1; j++) {
            if (arr[i][j] == arr[i][j+1]) {
                dist++;
            }
            else if (arr[i][j] == arr[i][j+1] - 1 && dist >= l) {
                dist = 1;
            }
            else if (arr[i][j] == arr[i][j+1] + 1 && dist >= 0) {
                dist = -l + 1;
            }
            else {
                break;
            }
        }
        if (j == n - 1 && dist >= 0) {
            cnt++;
        }
    }
    return cnt;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> l;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> a[i][j];
            b[j][i] = a[i][j];
        } 
    }

    answer = solve(a) + solve(b);
    cout << answer << "\n";

    return 0;
}