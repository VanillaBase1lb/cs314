# include <stdio.h>

int main(void) {
    int n, k, j, i, sum = 0;
    float mavg;
    /* FILL HERE */
    scanf("%d", &n);
    int a[n];
    for (i = 0; i < n; i++)
        scanf("%d", &a[i]); // reading array elements
    printf("Enter value of window size k:");
    scanf("%d", &k);
    for (i = 0; i < n - k + 1; i++) {
        /* FILL HERE */
        for (int j = 0; j < k; j++) {
            printf("%d ", a[j + i]);
        }
        printf("\n");
    }
    return 0;
}
