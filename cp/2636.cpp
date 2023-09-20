#include <bits/stdc++.h>
using namespace std;

bool flag;
int n, m, arr[104][104], visited[104][104];
int answer, cnt;
vector<pair<int, int>> temp;

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};


void dfs(int y, int x) {
    visited[y][x] = 1;
    if (arr[y][x] == 1) {
        temp.push_back({y, x});
        return;
    }
    for(int d = 0; d < 4; d++) {
        int ny = y + dy[d];
        int nx = x + dx[d];

        if(ny >= 0 && ny < n && nx >= 0 && nx < m) {
            if(visited[ny][nx] == 0) {
                dfs(ny, nx);
            }
        }
    }

    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> arr[i][j];
        }
    }

    while(true) {
        cnt = 0;
        fill(&visited[0][0], &visited[0][0] + 104 * 104, 0);
        temp.clear();
        dfs(0, 0);

        for(pair<int, int> i : temp) {
            cnt++;
            arr[i.first][i.second] = 0;
        }

        flag = 0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < m; j++) {
                if(arr[i][j] == 1) {
                    flag = 1;
                }
            }
        }
        answer++;
        if(flag == 0) break;
    }


    cout << answer << "\n";
    cout << cnt << "\n";
    return 0;
}