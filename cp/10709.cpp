#include <bits/stdc++.h>
using namespace std;

int h, w, answer[101][101];
string s, arr[101][101];

void mv(int i, int j) {
    while(true) {
        j++;
        if(j == w) return;
        if(arr[i][j] == "c") return;
        answer[i][j] = answer[i][j-1] + 1;
    }
    return;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> h >> w;

    for(int i = 0; i < h; i++) {
        cin >> s;
        for(int j = 0; j < w; j++) {
            arr[i][j] = s[j];
        }
    }

    for(int i = 0; i < h; i++) {
        for(int j = w-1; j > -1; j--) {
            if(arr[i][j] == "c") {
                mv(i, j);
            }
            else{
                answer[i][j] = -1;
            }
        }
    }

    for(int i = 0; i < h; i++) {
        for(int j = 0; j < w; j++) {
            cout << answer[i][j] << " ";
        }
        cout << "\n";
    }

    return 0;
}