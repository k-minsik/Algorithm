#include <bits/stdc++.h>
using namespace std;

int n, ret;

int func(int a) {
    ret = ret * a;

    if(a == n) {
        return ret;
    }
    
    a++;
    return func(a);
}

int main() {
    ios_base::sync_with_stdio(0);
    cin.tie(0); cout.tie(0);

    cin >> n;
    if (n == 0) {
        cout << 1 << "\n";
        return 0;
    }

    ret = 1;
    cout << func(1) << "\n";

    return 0;
}