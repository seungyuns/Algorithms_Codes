<h1> 이진탐색 </h1>

<h3>&nbsp;&nbsp;1. 오름차순 정렬이 되어있다고 가정한다.</h3>


```cpp
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#pragma warning(disable:4996)

int binary(int arr[], int s, int e, int value) {
	
	//기저조건
	if (s > e) {  
		return -1;
	}
	
	else if (s == e) {
		if (arr[s] == value) {
			return s;
		}
		else {
			return -1;
		}
	}
  
	else {
		int mid = (e + s) / 2;
 	  	
		if (arr[mid] == value) {
			return mid;
		}
		else if (value > arr[mid]) {
			return binary(arr, mid + 1, e, value);
		}
		else {
			return binary(arr, s, mid - 1, value);
		}
	}
}

int main(void) {
	int n, m;
	int arr[100001];
	int s[100001];
  
	scanf("%d %d", &n, &m);
	//정렬 되어있는것으로 가정
	for (int i = 0; i < n; i++) {
		scanf(" %d", &arr[i]);
	}

	for (int i = 0; i < m; i++) {
		scanf(" %d", &s[i]);
	}

	for (int i = 0; i < m; i++) {

		int inx = binary(arr, 0, n - 1, s[i]);

		if (inx == -1) {
			printf("NO");
		}
		else {
			printf("YES");
		}

		printf("\n");
	}

	return 0;
}
```


