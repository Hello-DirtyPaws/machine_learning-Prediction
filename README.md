# machine_learning-Prediction
It learns on 67% of the data and tests itself on the remaining data.

Inorder to run the code one any of the two files given (x.csv and international-airline-passengers.csv) just comment/uncomment line 13 and line 14.


The program takes in the input from a csv file and only works with one row at a given time. It initially splits the entire dataset into two parts; 67% and 33% roughly. 67% part of the dataset is for the algorithm to learn and the remaining part will be the one on which it will test itself. The algorithm learns using Long Short-Term Memory blocks (LSTM). It basically stores all the memory of its predictions and actual outputs. In order to compute the entry at any time(t), the program will look back at time (t-1) and check its block(memory) and it checks all blocks recursively. Then the current prediction is compared with the actual outcome and it becomes a block by itself too, making a step for future predictions of the entry with respect to time.

The output is presented as a graph: blue line -> original data, orange line -> training output and green line -> predicted output.

The algorithm works better with large dataset and it will adopt the linear scale optimization for way too off-beat series.

(The credit for the algorithm goes to Jason Brownlee).
