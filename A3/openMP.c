// file: main.c
#include <stdio.h>      // Standard I/O functions
#include <stdlib.h>     // Standard library functions (not strictly needed here)
#include <omp.h>        // OpenMP parallelism header

#define N 100           // Total number of elements in the array
#define NUM_PROCESSORS 4  // Number of threads (processors) to use for parallelism

int main() {
    int arr[N];                         // Array to store N elements
    int sum = 0;                        // Variable to store the final sum
    int PARTIAL_SUM[NUM_PROCESSORS] = {0};  // Array to store sum computed by each thread, initialized to 0

    // Initialize the array with values 0 to N-1
    for (int i = 0; i < N; i++) {
        arr[i] = i;
    }

    // Start parallel region using OpenMP with specified number of threads
    #pragma omp parallel num_threads(NUM_PROCESSORS)
    {
        int thread_id = omp_get_thread_num(); // Get the thread's unique ID (0 to NUM_PROCESSORS-1)

        // Compute the range of the array that this thread will sum
        int start = thread_id * (N / NUM_PROCESSORS);           // Start index for this thread
        int end = (thread_id + 1) * (N / NUM_PROCESSORS);       // End index (exclusive) for this thread

        // Compute partial sum for this thread's chunk of the array
        for (int i = start; i < end; i++) {
            PARTIAL_SUM[thread_id] += arr[i];
        }
    }

    // After the parallel region, aggregate the partial sums from each thread
    for (int i = 0; i < NUM_PROCESSORS; i++) {
        sum += PARTIAL_SUM[i];  // Add each thread's result to the total sum
        printf("Partial sum from thread %d: %d\n", i, PARTIAL_SUM[i]);  // Print each thread's contribution
    }

    // Print the final total sum
    printf("Total Sum: %d\n", sum);

    return 0;  // Indicate successful program termination
}




//Terminal commands

//windows:
// gcc -fopenmp openMP.c -o output.exe
// .\output.exe

//linux:
//gcc -fopenmp main.c -o output
//./output