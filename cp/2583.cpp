#include <bits/stdc++.h>
using namespace std;

int m, n, k, arr[101][101], visited[101][101], nx, ny, s, y, x; 
int a, b, c, d;

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};

int dfs(int sy, int sx, int s) {
    vector<pair<int, int>> st;
    st.push_back({sy, sx});
    s = 1;

    while(st.size()) {
        tie(y, x) = st.back(); st.pop_back();

        for(int d = 0; d < 4; d++) {
            ny = y + dy[d];
            nx = x + dx[d];

            if(ny >= 0 && ny < n && nx >= 0 && nx < m) {
                if(arr[ny][nx] == 0 && visited[ny][nx] == 0) {
                    visited[ny][nx] = 1;
                    st.push_back({ny, nx});
                    s++;
                }
            }
        }
    }
    return s;
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    vector<int> cnt;

    cin >> m >> n >> k;

    for(int i = 0; i < k; i++) {
        cin >> a >> b >> c >> d;

        for(int y = a; y < c; y++) {
            for(int x = b; x < d; x++) {
                arr[y][x] = 1;
            }
        }
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
            if(arr[i][j] == 0 && visited[i][j] == 0) {
                s = 0;
                visited[i][j] = 1;
                s = dfs(i, j, s);
                cnt.push_back(s);
            }
        }
    }

    sort(cnt.begin(), cnt.end());
    cout << cnt.size() << "\n";
    for(int i : cnt) cout << i << " ";

    return 0;
}