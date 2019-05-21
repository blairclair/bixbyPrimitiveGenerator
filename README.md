# bixbyPrimitiveGenerator
A python script that will generate primitive files for a samsung bixby capsule when passed json data.

How to use
----------------
----------------
1. clone the repo using git clone https://github.com/blairclair/bixbyPrimitiveGenerator.git *filename* .
2. If you do not have a models folder already created in your capsule, create one and move parser.py into it.
3. Open parser.py and replace the line 
```
    with open("ditto.json") as f:  
```
with
```
    with open(*your filename with json data*) as f:
```    
4. Run the script with *python parser.py*

Testing
--------
I have provided the file ditto.json for anyone who merely wishes to test the script with random json data. If this is your goal you can skip step 3.

Example
--------
The results of running parser.py on ditto.json are stored inside of the results folder.
