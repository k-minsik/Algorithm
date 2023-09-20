#include <bits/stdc++.h>
using namespace std;

int r, c;
char arr[1504][1504];
string s;
vector<pair<int, int>> bird;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> r >> c;
    for(int i = 0; i < r; i++) {
        cin >> s;
        for(int j = 0; j < c; j++) {
            arr[i][j] = s[j];
            if(arr[i][j] == 'L') {
                bird.push_back({i, j});
            }
        }
    }



    return 0;
}