#include <bits/stdc++.h>
using namespace std;

int n, m;
string monster, quiz;
map<string, int> book;
map<int, string> book2;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n >> m;

    for(int i = 1; i <= n; i++) {
        cin >> monster;
        book[monster] = i;
        book2[i] = monster;
    }

    for(int i = 0; i < m; i++) {
        cin >> quiz;
        if(atoi(quiz.c_str()) == 0) cout << book[quiz] << "\n";
        else cout << book2[atoi(quiz.c_str())] << "\n";
    }

    return 0;
}