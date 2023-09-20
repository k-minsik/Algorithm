#include <bits/stdc++.h>
using namespace std;

int n, res;
string s; 

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);

    cin >> n;

    for(int i = 0; i < n; i++) {
        cin >> s;
        stack<char> stack_;
        for(char c : s) {
            if(stack_.size() && stack_.top() == c) stack_.pop();
            else stack_.push(c);
        }
        if(stack_.size() == 0) res++;
    }

    cout << res << "\n"

    return 0;
}