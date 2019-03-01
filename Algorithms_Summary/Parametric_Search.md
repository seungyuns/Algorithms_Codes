<h1>Parametric_Search</h1>

<h3> &nbsp; &nbsp; 1. 조건을 만족하는 개수와 만족하지 않는 개수의 경계를 이진탐색으로 찾는다 </h3>

```cpp

#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#pragma warning(disable:4996)

typedef enum {
	false = 0,
	true = 1
} bool;

int MAX = 10005;
int n;
int S;
int data[10005];

bool check(int interval) {
	// 1 2 3 4 5 6 7 8 9   8
	int sum = 0;

	for (int i = 0; i < interval; i++) {
		sum += data[i];
	}
	if (sum >= S) return true;

	for (int i = 0; i < n - interval; i++) {
		sum = sum - data[i] + data[i + interval];

		if (sum >= S) return true;
	}

	return false;
}

int main(void) {


	scanf("%d %d", &n, &S);

	for (int i = 0; i < n; i++) {
		scanf("%d", &data[i]);
	}

	int start = 1;
	int end = n;

	if (check(1)) {
		printf("0");
	}
	if (!check(n)) {
		printf("False");
	}

	while (start + 1 < end) {
		int mid = (start + end) / 2;
		if (check(mid)) {
			end = mid;
		}
		else {
			start = mid;

		}
	}
	printf("%d", end);

}
```
