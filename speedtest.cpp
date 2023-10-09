#include <iostream>
#include <chrono>

int main() {
    auto start = std::chrono::high_resolution_clock::now();

    for (int i = 1; i <= 1000000000; ++i) {
        std::cout << i << std::endl;
    }

    auto end = std::chrono::high_resolution_clock::now();
    auto duration = std::chrono::duration_cast<std::chrono::seconds>(end - start);

    std::cout << "Total time taken: " << duration.count() << " seconds" << std::endl;

    return 0;
}
