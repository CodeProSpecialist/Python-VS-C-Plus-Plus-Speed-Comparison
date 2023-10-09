Speed test race between Python and C++ 

Print the total time taken in seconds to finish counting to ten million. 

My computer took 25 seconds for C++ and 41.51 seconds for Python3 without pycuda. 

Pycuda for Python3 should be much faster than C++. 

For Linux, compile the C++ code into a runnable binary object with the following command: 

g++ -o speedtest speedtest.cpp

Then run on command line:

./speedtest

_____________________________________________________________

Run the Python code with the command:

python3 speedtest.py

pip3 install pycuda      # (for Nvidia video #cards only that have cuda cores )

python3 python-cuda-speedtest.py
