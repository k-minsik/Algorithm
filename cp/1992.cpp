#include <bits/stdc++.h>
using namespace std;

int n, arr[65][65];
string temp, res;

string f(int y, int x, int size) {
    string tmp = "";
    char a = arr[y][x];
    if(size == 1) {
        return string(1, arr[y][x]);
    }
    else {
        for(int i = y; i < y + size; i++) {
            for (int j = x; j < x + size; j++) {
                if(arr[i][j] != a){
                    tmp += "(";
                    tmp += f(y, x, size/2);
                    tmp += f(y, x + size/2, size/2);
                    tmp += f(y + size/2, x, size/2);
                    tmp += f(y + size/2, x + size/2, size/2);
                    tmp += ")";
                    return tmp;
                }
            }
        }
    }

    return string(1, arr[y][x]);
}


int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;
    for(int i = 0; i < n; i++) {
        cin >> temp;
        for(int j = 0; j < n; j++) {
            arr[i][j] = temp[j];
        }
    }

    res = f(0, 0, n);
    cout << res << "\n";
    return 0;
}