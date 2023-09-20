#include <bits/stdc++.h>
using namespace std;

int n, m, arr[1001][1001], visited[1001][1001], ret, y, x;
int dy[] = {-1, 0, 1, 0}, dx[] = {0, 1, 0, -1};
queue<pair<int, int>> to;

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> m;
    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            cin >> arr[i][j];
            if (arr[i][j] == 1) {
                to.push({i, j});
            }
        }
    }

    while (to.size()) {
        tie(y, x) = to.front();
        to.pop();
        visited[y][x] = 1;

        for(int d = 0; d < 4; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];

            if (ny >= 0 && ny < m && nx >= 0 && nx < n) {
                if (arr[ny][nx] == 0 && visited[ny][nx] == 0) {
                    arr[ny][nx] = arr[y][x] + 1;
                    to.push({ny, nx});
                }
            }
        }
    }

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if (arr[i][j] == 0) {
                cout << -1 << "\n";
                return 0;
            }
            else {
                if (arr[i][j] > ret) {
                    ret = arr[i][j];
                }
            }
        }
    }
    cout << ret - 1 << "\n";
    return 0;
}