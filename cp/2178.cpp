#include <bits/stdc++.h>
using namespace std;

int n, m, graph[104][104], y, x, ny, nx;
string s;
deque<pair<int, int>> dq;
const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;

    for(int i = 0; i < n; i++){
        cin >> s;
        for(int j = 0; j < m; j++){
            graph[i][j] = s[j] - '0';
        }
    }

    dq.push_back({0, 0});
    while(dq.size()) {
        tie(y, x) = dq.front();
        dq.pop_front();

        for(int i = 0; i < 4; i++) {
            ny = y + dy[i];
            nx = x + dx[i];

            if(ny >= 0 && ny < n && nx >= 0 && nx < m) {
                if(graph[ny][nx] == 1) {
                    dq.push_back({ny, nx});
                    graph[ny][nx] += graph[y][x];
                }
            }

        }
    }

    cout << graph[n-1][m-1] << "\n";

    return 0;
}