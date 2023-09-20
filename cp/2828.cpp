#include <bits/stdc++.h>
using namespace std;

int n, m, j, answer, apple, l, r, temp;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;
    cin >> j;

    l = 1;
    for(int i = 0; i < j; i++) {
        r = l + m - 1;
        cin >> apple;

        if(apple >= l && apple <= r) continue;
        else if(apple < l) {
            temp = l - apple;
            l -= temp;
            answer += temp;
        }
        else if(apple > r) {
            temp = apple - r;
            l += temp;
            answer += temp;
        }
    }

    cout << answer << "\n";
    return 0;
}