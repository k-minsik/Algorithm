#include <bits/stdc++.h>
using namespace std;

int fee, a, b, c, t1, t2;
int arr[101];

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    cin >> a >> b >> c;

    for(int i = 0; i < 3; i++){
        cin >> t1 >> t2;
        for(int j = t1; j < t2; j++) {
            arr[j]++;
        }
    }

    for(int i : arr) {
        if(i == 1) fee += a;
        else if(i == 2) fee += b*2;
        else if(i == 3) fee += c*3;
    }

    cout << fee;

    return 0;
}