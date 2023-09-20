#include <bits/stdc++.h>
using namespace std;

int n, arr[101][101], visited[101][101], cnt, y, x, l, answer;
const int dy[] = {-1, 0, 1, 0};
const int dx[] = {0, 1, 0, -1};

void bfs(int y, int x, int k) {
    queue<tuple<int, int, int>> q;
    q.push({y, x, 0});

    while(q.size()) {
        tie(y, x, l) = q.front();
        q.pop();

        for(int d = 0; d < 4; d++) {
            int ny = y + dy[d];
            int nx = x + dx[d];

            if(ny >= 0 && ny < n && nx >= 0 && nx < n) {
                if(arr[ny][nx] == 0 && visited[ny][nx] == 0){
                    visited[ny][nx] = 1;
                    q.push({ny, nx, l + 1});
                }
                else if(arr[ny][nx] != 0 && arr[ny][nx] != k){
                    answer = min(answer, l);
                }
            }
        }

    }

    return ;
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cin >> arr[i][j];
        }
    }
    
    // 섬 번호 붙이기
    vector<pair<int, int>> st;
    cnt = 1;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if(arr[i][j] == 1 && visited[i][j] == 0) {
                st.push_back({i, j});
                visited[i][j] = 1;
                arr[i][j] = cnt;
                while(st.size()) {
                    tie(y, x) = st.back();
                    st.pop_back();

                    for(int d = 0; d < 4; d++) {
                        int ny = y + dy[d];
                        int nx = x + dx[d];
                        if(ny >= 0 && ny < n && nx >= 0 && nx < n) {
                            if(arr[ny][nx] == 1 && visited[ny][nx] == 0) {
                                arr[ny][nx] = cnt;
                                visited[ny][nx] = 1;
                                st.push_back({ny, nx});
                            }
                        }
                    }
                }
                cnt++;
            }
        }
    }

    // 섬 확장
    answer = 1e9;
    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            if (arr[i][j]) {
                fill(&visited[0][0], &visited[0][0] + 101 * 101, 0);
                bfs(i, j, arr[i][j]);
            }
        }
    }
    cout << answer << "\n";

    return 0;
}