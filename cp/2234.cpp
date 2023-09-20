#include <bits/stdc++.h>
using namespace std;

int n, m, arr[51][51], visited[51][51], roomsize[2501];
int room, big, biggest;
int dy[4] = {0, -1, 0, 1}, dx[4] = {-1, 0, 1, 0};

int dfs(int y, int x, int room) {
    if (visited[y][x]) return 0;
    
    int ret = 1;
    visited[y][x] = room;
    for(int i = 0; i < 4; i++) {
        if(!(arr[y][x] & (1  << i))) {
            int ny = y + dy[i];
            int nx = x + dx[i];
            ret += dfs(ny, nx, room);
        }
    }

    return ret;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n >> m;

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            cin >> arr[i][j];    
        }
    }

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if(!visited[i][j]) {
                room++;
                roomsize[room] = dfs(i, j, room);
                big = max(big, roomsize[room]);
            }
        }
    }

    for(int i = 0; i < m; i++) {
        for(int j = 0; j < n; j++) {
            if (i + 1 < m) {    
                int top = visited[i][j];
                int bottom = visited[i+1][j];
                if (top != bottom) {
                    biggest = max(biggest, roomsize[top] + roomsize[bottom]);
                }
            }

            if (j + 1 < n) {
                int left = visited[i][j];
                int right = visited[i][j+1];
                if (left != right) {
                    biggest = max(biggest, roomsize[left] + roomsize[right]);
                }
            }
        }
    }


    cout << room << "\n";
    cout << big << "\n";
    cout << biggest << "\n";

    return 0;
}