# CryptocurrencyPrediction-with-GRU

GRU for Bitcoin Price Prediction 

This repo is adapted from the program of https://github.com/khuangaf/CryptocurrencyPrediction for Google colab. 

Google colab supplies the following environments.    


Python 3.6.9  
Tensorflow=2.3.0  
Keras=2.4.3  
Pandas=1.1.5  
Numpy=1.18.5  
h5py=2.10.0  
sklearn=0.0  

File Illustration  


tocsv.py : convert price of bitcoin from json to csv  
tohdf5.py : convert price of bitcoin from csv to hdf5  
GRU.py : training with GRU (tan+ReLU)  
plot-GRU.py : plot results of training   
bitcoin-2018-2020-full.h5 : bitcoin price between 2018 and 2020 in HDF5  
bitcon-2018-2020-93pct.h5 : 93% of the above, 7% is used for validation only  


![fig2](https://user-images.githubusercontent.com/15276052/102293710-f9910680-3f8a-11eb-946f-a47778a6fae8.png)
