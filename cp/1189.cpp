#include <bits/stdc++.h>
using namespace std;

int r, c, k, visited[6][6];
char arr[6][6];
int dy[4] = {-1, 0, 1, 0}, dx[4] = {0, 1, 0, -1};
string s;

int go(int y, int x) {
    if(y == 0 && x == c-1) {
        if(visited[y][x] == k) {
            return 1;
        }
        else{
            return 0;
        }
    }

    int ret = 0;
    for(int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];
        if(ny >= 0 && ny < r && nx >= 0 && nx < c) {
            if(visited[ny][nx] == 0 && arr[ny][nx] != 'T') {
                visited[ny][nx] = visited[y][x] + 1;
                ret += go(ny, nx);
                visited[ny][nx] = 0;
            }
        }
    }

    return ret;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> r >> c >> k;
    for(int i = 0; i < r; i++) {
        cin >> s;
        for(int j = 0; j < c; j++) {
            arr[i][j] = s[j];
        }
    }

    visited[r-1][0] = 1;
    cout << go(r-1, 0) << "\n";

    return 0;
}