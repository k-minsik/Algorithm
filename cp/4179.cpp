#include <bits/stdc++.h>
using namespace std;

int n, m, jy, jx, y, x;
int fire_map[1004][1004], out_map[1004][1004];
char arr[1004][1004];
queue<pair<int, int>> fire, out;

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    fill(&fire_map[0][0], &fire_map[0][0] + 1004 * 1004, 1e9);

    cin >> n >> m;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            cin >> arr[i][j];
            if(arr[i][j] == 'F') {
                fire.push({i, j});
                fire_map[i][j] = 1;
            }
            else if(arr[i][j] == 'J') {
                out.push({i, j});
                out_map[i][j] = 1;
            }
        }
    }

    while(fire.size()) {
        tie(y, x) = fire.front();
        fire.pop();

        for(int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            
            if(ny >= 0 && ny < n && nx >= 0 && nx < m) {
                if(fire_map[ny][nx] == 1e9 && arr[ny][nx] != '#') {
                    fire_map[ny][nx] = fire_map[y][x] + 1;
                    fire.push({ny, nx});
                }
            }
        }
    }

    int answer = 0;
    while(out.size()) {
        tie(y, x) = out.front();
        out.pop();

        if(y == 0  || y == n - 1 || x == 0 || x == m - 1){
            answer = out_map[y][x];
            break;
		}

        for(int i = 0; i < 4; i++) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            
            if(ny >= 0 && ny < n && nx >= 0 && nx < m) {
                if(arr[ny][nx] != '#' && out_map[ny][nx] == 0) {
                    if(fire_map[ny][nx] > out_map[y][x] + 1) {
                        out_map[ny][nx] = out_map[y][x] + 1;
                        out.push({ny, nx});
                    }
                }
            }
        }
    }

    if(answer != 0) cout << answer << "\n";
    else cout << "IMPOSSIBLE\n";

    return 0;
}