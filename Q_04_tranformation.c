#include <stdio.h>
#include<stdlib.h>
#include<math.h>
#include<time.h>

float fun( float x) // Transformation function
{
	return - 0.5 * log(x) ;
}

 int main()
{
	int n = 100000 ;
	float uni_rand ;
	time_t t ;

	//initialize the Linear Congruential random number generater giving the seed
	srand((unsigned) time(&t)) ;
	
	// Prints n exponentially distributed random number by transformation method
	for (int i = 0; i < n; i++)
	{
		// uniformly distributed random no between 0 and 1
		uni_rand = rand()/(float) RAND_MAX ;
		
		printf("%f \n", fun(uni_rand));
	}
	return 0;
}