#include <iostream>
#include <vector>
#include <sstream>
using namespace std;

int main() {
    int K;
    cin >> K;
    for (int i = 0; i < K; i++) {
        int C, B, n, r;
        cin >> C >> B >> n >> r;
        cin.ignore();

        vector<int> rescued;
        if (B > 0) {
            string line;
            getline(cin, line);
            istringstream iss(line);
            int x;
            while (iss >> x) rescued.push_back(x);
        }

        vector<bool> isRescued(C + 1, false);
        for (int x : rescued) isRescued[x] = true;

        int res = 0;
        for (int i = 0; i < n; i++) {
            int ci, pi;
            cin >> ci >> pi;
            if (isRescued[ci]) {
                res += (pi * r) / 100;
            }
        }

        cout << "Data Set " << i + 1 << ":\n";
        cout << res << "\n\n";
    }
    return 0;
}
