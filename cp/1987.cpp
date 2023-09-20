#include <bits/stdc++.h>
using namespace std;

int r, c, visited[27], answer;
char arr[21][21];

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};

void dfs(int y, int x, int d) {
    answer = max(answer, d);
    for(int i = 0; i < 4; i++) {
        int ny = y + dy[i];
        int nx = x + dx[i];

        if(ny >= 0 && ny < r && nx >= 0 && nx < c) {
            int temp = arr[ny][nx] - 'A';
            if(visited[temp] == 0) {
                visited[temp] = 1;
                dfs(ny, nx, d + 1);
                visited[temp] = 0;
            }
        }
    }

    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> r >> c;

    for(int i = 0; i < r; i++) {
        for(int j = 0; j < c; j++) {
            cin >> arr[i][j];
        }
    }
    
    visited[arr[0][0] - 'A'] = 1;
    dfs(0, 0, 1);

    cout << answer << "\n";
    return 0;
}