#include <bits/stdc++.h>
using namespace std;
int n, ret=1e9, arr[20][20], visited[20][20];
const int dy[4] = {-1, 1, 0, 0}, dx[4] = {0, 0, -1, 1};

bool check(int y, int x) {
    if(visited[y][x]) {
        return false;
    }

    for(int d = 0; d < 4; d++) {
        int ny = y + dy[d];
        int nx = x + dx[d];
        if(visited[ny][nx]) {
            return false;
        }
    }

    return true;
}

void go(int cnt, int temp) {
    if (cnt == 3) {
        ret = min(ret, temp);
        return;
    }
    for(int i = 1; i < n-1; i++) {
        for(int j = 1; j < n-1; j++) {
            if(check(i, j)) {
                int temp2 = arr[i][j];
                visited[i][j] = 1;
                for (int d = 0; d < 4; d++) {
                    int ni = i + dy[d];
                    int nj = j + dx[d];
                    visited[ni][nj] = 1;
                    temp2 += arr[ni][nj];
                }
                go(cnt + 1, temp + temp2);
                visited[i][j] = 0;
                for (int d = 0; d < 4; d++) {
                    int ni = i + dy[d];
                    int nj = j + dx[d];
                    visited[ni][nj] = 0;
                }
            }
                
        }
    }
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    go(0, 0);
    
    cout << ret << "\n";

    return 0;
}