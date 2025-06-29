#include <stdio.h>

int main() {
    int A, K;
    scanf("%d %d", &A, &K);

    int arr[10001];  
    for (int i = 0; i < A; i++) {
        scanf("%d", &arr[i]);
    }

    int V = 0;
    int res1 = -1, res2 = -1;

    for (int i = 0; i < A; i++) {
        for (int j = 0; j < A - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                V++;
                if (V == K) {
                    res1 = arr[j];
                    res2 = arr[j + 1];
                }
                
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }

    if (res1 != -1) {
        if (res1 < res2)
            printf("%d %d\n", res1, res2);
        else
            printf("%d %d\n", res2, res1);
    } else {
        printf("-1\n");
    }

    return 0;
}
