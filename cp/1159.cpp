#include <bits/stdc++.h>
using namespace std;

string mem, res;
int cnt[26], n;

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> mem;
        cnt[mem[0] - 'a']++;
    }

    for(int j = 0; j < 26; j++) {
        if(cnt[j] > 4) res += char(j + 'a');
    }

    if(res.size()) cout << res << "\n";
    else cout << "PREDAJA" << "\n";

    return 0;
}