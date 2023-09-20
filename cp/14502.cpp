#include <bits/stdc++.h>
using namespace std;

int n, m, arr[10][10], visited[10][10], answer, nx, ny;
vector<pair<int, int>> wall, virus;

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};

void dfs(int y, int x) {
    for(int d = 0; d < 4; d++) {
        ny = y + dy[d];
        nx = x + dx[d];

        if(ny >= 0 && ny < n && nx >= 0  && nx < m) {
            if(arr[ny][nx] != 1 && visited[ny][nx] == 0) {
                visited[ny][nx] = 1;
                dfs(ny, nx);
            }
        }
    }
    return;
}

int solution() {
    int cnt = 0;

    fill(&visited[0][0], &visited[0][0] + 10 * 10, 0);
    for(pair<int, int> i : virus) {
        visited[i.first][i.second] = 1;
        dfs(i.first, i.second);
    }

    for(int j = 0; j < n; j++) {
        for(int k = 0; k < m; k++) {
            if(arr[j][k] == 0 && visited[j][k] == 0) cnt++;
        }
    }

    return cnt;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> arr[i][j];
            if(arr[i][j] == 2) virus.push_back({i, j});
            if(arr[i][j] == 0) wall.push_back({i, j});
        }
    }

    for(int i = 0; i < wall.size(); i++) {
        for(int j = 0; j < i; j++) {
            for(int k = 0; k < j; k++) {
                arr[wall[i].first][wall[i].second] = 1;
                arr[wall[j].first][wall[j].second] = 1;
                arr[wall[k].first][wall[k].second] = 1;
                answer = max(answer, solution());
                arr[wall[i].first][wall[i].second] = 0;
                arr[wall[j].first][wall[j].second] = 0;
                arr[wall[k].first][wall[k].second] = 0;

            }
        }
    }

    cout << answer << "\n";
    return 0;
}
