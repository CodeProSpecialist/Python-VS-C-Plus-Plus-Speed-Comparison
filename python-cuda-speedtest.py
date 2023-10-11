import pycuda.driver as cuda
import pycuda.autoinit
from pycuda.compiler import SourceModule
import time

# CUDA kernel code
cuda_code = """
__global__ void count_to_10_million(int *result) {
    int tid = threadIdx.x + blockIdx.x * blockDim.x;
    if (tid < 10000000) {
        result[tid] = tid + 1;
    }
}
"""

# Compile the CUDA kernel
module = SourceModule(cuda_code)
count_kernel = module.get_function("count_to_10_million")

# Create an array on the GPU to store the results
result_gpu = cuda.mem_alloc(10000000 * 4)  # 4 bytes per int

# Start measuring time
start_time = time.time()

# Launch the CUDA kernel
block_size = 256
grid_size = (10000000 + block_size - 1) // block_size
count_kernel(result_gpu, block=(block_size, 1, 1), grid=(grid_size, 1))

# Copy the results back from GPU to CPU
result_cpu = bytearray(4 * 10000000)
cuda.memcpy_dtoh(result_cpu, result_gpu)

# End measuring time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time

# Print all numbers from 1 to 10,000,000, one number per line
for i in range(10000000):
    print(int.from_bytes(result_cpu[i * 4:(i + 1) * 4], byteorder='little'))

# Print the total time taken
print("Total time taken:", elapsed_time, "seconds")

# Clean up
result_gpu.free()
