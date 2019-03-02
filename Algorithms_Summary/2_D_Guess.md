<h1> 이차식 정답 추론 </h1>

<h3>&nbsp;&nbsp;1. int와 int 의 곱은 잠시 int형으로 저장되기 때문에, 이과정에서 범위를 벗어난다면, 다른 형식에도 올바르게 대입되지 않는다.</h3>
<h3>&nbsp;&nbsp;2. 기저 조건에 주의한다. ( s > e )의 예외 상황이 항상 발생한다. (int 정수형으로 나누기 때문에) </h3>

```cpp
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include<string.h>
#pragma warning(disable:4996)

long long N;

int guess(long long s, long long e) {

	if (s > e) {
		return e;
	}
	else if (s == e) {
		long long result = s * s + s;
		if (result > N) {
			return e - 1;
		}
		else {
			return e;
		}
	}
	else {

		long long mid = (s + e) / 2;
		long long result = mid * mid + mid;
		
		printf("\n%lld \n", mid);
		printf("\n%lld \n", result);

		if (result == N) {
			return mid;
		}
		else if (result > N) {
			guess(s, mid - 1);
		}
		else {
			guess(mid + 1, e);
		}
	}
}

int main(void) {

	int s = 1;
	int e = 1000000000;

	scanf("%lld", &N);

	int c = guess(s, e);

	printf("\n\n");
	printf("%d", c);
}

```
![two_d_guess_quiz](/img/two_d_guess.JPG)
