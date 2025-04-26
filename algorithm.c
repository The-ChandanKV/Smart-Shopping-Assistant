#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX 100

typedef struct {
    char name[100];
    int price;
    int value;
    char link[300];
} Item;

Item items[MAX];
int dp[MAX][MAX];

int main() {
    FILE *fin = fopen("input.txt", "r");
    FILE *fout = fopen("output.txt", "w");

    int n, budget;
    fscanf(fin, "%d %d", &n, &budget);

    for (int i = 0; i < n; i++) {
        fscanf(fin, " %[^\n] %d %d %[^\n]", items[i].name, &items[i].price, &items[i].value, items[i].link);
    }

    for (int i = 0; i <= n; i++) {
        for (int w = 0; w <= budget; w++) {
            if (i == 0 || w == 0)
                dp[i][w] = 0;
            else if (items[i - 1].price <= w)
                dp[i][w] = (dp[i - 1][w] > (dp[i - 1][w - items[i - 1].price] + items[i - 1].value)) 
                           ? dp[i - 1][w] 
                           : (dp[i - 1][w - items[i - 1].price] + items[i - 1].value);
            else
                dp[i][w] = dp[i - 1][w];
        }
    }

    int w = budget;
    fprintf(fout, "Selected Items:\n");
    for (int i = n; i > 0 && w > 0; i--) {
        if (dp[i][w] != dp[i - 1][w]) {
            fprintf(fout, "%s %d %d %s\n", items[i - 1].name, items[i - 1].price, items[i - 1].value, items[i - 1].link);
            w -= items[i - 1].price;
        }
    }

    fclose(fin);
    fclose(fout);
    return 0;
}
