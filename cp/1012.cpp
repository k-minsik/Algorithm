#include <bits/stdc++.h>
using namespace std;

int t, m, n, k, x, y, nx, ny, a, b, res;
int arr[54][54], visited[54][54];
deque<pair<int, int>> dq;

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};

void dfs(int y_, int x_) {
    dq.push_back({y_, x_});
    visited[y_][x_] = 1;

    while(dq.size()) {
        tie(y, x) = dq.back(); dq.pop_back();
        visited[y][x] = 1;

        for(int d = 0; d < 4; d++) {
            ny = y + dy[d];
            nx = x + dx[d];

            if(ny >= 0 && ny < n && nx >= 0 && nx < m) {
                if(arr[ny][nx] == 1 && visited[ny][nx] == 0) {
                    dq.push_back({ny, nx});
                }
            }
        }
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> t;

    for(int t_ = 0; t_ < t; t_++) {
        cin >> m >> n >> k;
        fill(&arr[0][0], &arr[0][0] + 54 * 54, 0);
        fill(&visited[0][0], &visited[0][0] + 54 * 54, 0);
        for(int k_ = 0; k_ < k; k_++) {
            cin >> a >> b;
            arr[b][a] = 1;
        }

        res = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(arr[i][j] == 1 && visited[i][j] != 1) {
                    dfs(i, j);
                    res++;
                }
            }
        }
        cout << res << "\n";
    }

    return 0;
}