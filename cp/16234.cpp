#include <bits/stdc++.h>
using namespace std;

int n, l, r, arr[54][54], visited[54][54], cnt, sum;
vector<pair<int, int>> temp;

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};

void bfs(int y, int x) {
    queue<pair<int, int>> q;
    q.push({y, x});
    temp.push_back({y, x});
    visited[y][x] = 1;

    while (q.size()) {
        tie(y, x) = q.front();
        q.pop();

        for(int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];

            if(ny >= 0 && ny < n && nx >= 0 && nx < n) {
                if(visited[ny][nx] == 0) {
                    if(abs(arr[y][x] - arr[ny][nx]) >= l && abs(arr[y][x] - arr[ny][nx]) <= r) {
                        visited[ny][nx] = 1;
                        sum += arr[ny][nx];
                        q.push({ny, nx});
                        temp.push_back({ny, nx});
                    }
                }
            }
        }
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(0); cout.tie(0);

    cin >> n >> l >> r;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }

    while(true) {
        int flag = 0;
        fill(&visited[0][0], &visited[0][0] + 54 * 54, 0);
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(visited[i][j] == 0){
                    temp.clear();
                    sum = arr[i][j];
                    bfs(i, j);
                    if(temp.size() > 1) {
                        for(pair<int, int> t : temp) {
                            arr[t.first][t.second] = sum / temp.size();
                            flag = 1;
                        }
                    }
                }
            }
        }
        if(flag == 0) break;
        cnt++;
    }
    
    cout << cnt << "\n";
    return 0;
}