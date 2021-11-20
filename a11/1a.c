# include <stdio.h>

int main() {
    int a = 25, b = 7, c = 15, d;
    float m = 12.5, x, y;
    d = a + 3/ b * c;
    x = (float)(a/b);
    y = m * (b / c);
    c = a + b / c;
    printf("%d %d %f %f", c, d, x, y);
    return 0;
}
