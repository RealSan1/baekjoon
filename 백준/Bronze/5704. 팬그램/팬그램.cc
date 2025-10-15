#include <iostream>
#include <map>
#include <string>
using namespace std;

int main() {
    while (true)
    {
        string num;

        getline(cin, num);
        if (num == "*") break;

        map<char, int> alpha;
        for (int i=0; i < 26; i++) alpha['a'+i] = 0;
        

        for (char i : num) {
            if (isalpha(static_cast<unsigned char>(i))) {
                alpha[static_cast<unsigned char>(i)] = 1;
            }
        }

        bool hasZero = false;
        for (auto [ch, val] : alpha) {
            if (val == 0) {
                hasZero = true;
                break;
            }
        }

        if (hasZero) cout << 'N' << '\n';
        else cout << 'Y' << '\n';
        }
}