#include <bits/stdc++.h>
using namespace std;

int arr[101][101], visited[101][101], nx, ny, n, temp, res, answer;
int max_h = -1e9, min_h = 1e9;
string s;

const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};


void dfs(int y, int x, int h) {
    vector<pair<int, int>> st;
    st.push_back({y, x});

    while(st.size()) {
        tie(y, x) = st.back(); st.pop_back();
        visited[y][x] = 1;

        for(int d = 0; d < 4; d++) {
            ny = y + dy[d];
            nx = x + dx[d];

            if(ny >= 0 && ny < n && nx >= 0 && nx < n ) {
                if(arr[ny][nx] > h && visited[ny][nx] == 0) {
                    st.push_back({ny, nx});
                }
            }
        }
    }
    return;
} 


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> temp;
            min_h = min(min_h, temp);
            max_h = max(max_h, temp);
            arr[i][j] = temp;
        }
    }

    for(int h = min_h - 1; h < max_h; h++) {
        res = 0;
        fill(&visited[0][0], &visited[0][0] + 101 * 101, 0);
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                if(arr[i][j] > h && visited[i][j] == 0) {
                    dfs(i, j, h);
                    res++;
                }
            }
        }
        answer = max(answer, res);
    }

    cout << answer << "\n";
    return 0;
}