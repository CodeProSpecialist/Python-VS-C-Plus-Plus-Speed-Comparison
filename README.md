Speed test race between Python and C++ 

Print the total time taken in seconds to finish counting to ten million. 

My computer took 25 seconds for C++ and 41.51 seconds for Python3 without pycuda. 

Pycuda for Python3 is much faster than C++. 

Python with Pycuda took only 0.03 seconds to finish counting to ten million 
with 640 cuda core processors on an Nvidia video card. 

For Linux, compile the C++ code into a runnable binary object with the following command: 

g++ -o speedtest speedtest.cpp

Then run on command line:

./speedtest

_____________________________________________________________

Run the Python code with the command:

python3 speedtest.py

pip3 install pycuda      # (for Nvidia video #cards only that have cuda cores )

python3 python-cuda-speedtest.py
