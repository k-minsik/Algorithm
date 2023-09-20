#include <bits/stdc++.h>
using namespace std;

int a[9], sum;
int b, c;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);

    for(int i = 0; i < 9; i++){
        cin >> a[i];
        sum += a[i];
    }

    sort(a, a + 9);
    for(int i = 0; i < 8; i++){
        for(int j = i+1; j < 9; j++){
            if(sum - a[i] - a[j] == 100){
                b = i;
                c = j;
                break;
            }
        }
    }
    
    for(int i = 0; i < 9; i++){
        if(i == b || i == c) continue;
        else{
            cout << a[i] << " ";
        }
    }
    return 0;
}