#include <stdio.h>
#include <omp.h>
int main() {
    int a[] = {1, 2, 3, 4, 5}, sum = 0;

    #pragma omp parallel for reduction(+:sum)
    for (int i = 0; i < 5; i++) sum += a[i];
        printf("Sum: %d\n", sum);

    #pragma omp parallel for 
    for (int i = 0; i < 10; i++)
    {
        printf("i=%d by thread %d\n", i, omp_get_thread_num());
    }
    
    #pragma omp parallel
    {
        printf("Thread ID: %d\n", omp_get_thread_num());
    }
    return 0;
}



/* 

Commands - 
gcc -fopenmp file.c -o output
.\output.exe

*/
