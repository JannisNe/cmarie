# Compare stuff

Simple example of comparing python, cython and c.

## Instructions

Install via pip:

```bash
pip install .
```

Run `comparison.py`:

```bash
python comparison.py
```

## Results

Unoptimized C and Cython can be slower than Python. 

```
testing numba
running ...
 1 x 5 times ....
------------ numba ------------ 
  Result: 0.2500152587890625
  Min:  2.92e-07s
  Max:  4.04e-06s
  Mean: 8.46e-07s +/- 1.09e-06s


testing cython
running ...
 1000000 x 5 times ....
------------ cython ------------ 
  Result: 0.2500152587890625
  Min:  2.29e-07s
  Max:  2.31e-07s
  Mean: 2.30e-07s +/- 5.06e-10s


testing python
running ...
 100000 x 5 times ....
------------ python ------------ 
  Result: 0.25
  Min:  3.81e-06s
  Max:  3.87e-06s
  Mean: 3.84e-06s +/- 1.32e-08s


testing c
running ...
 500000 x 5 times ....
------------ c ------------ 
  Result: 0.2500038146972656
  Min:  5.58e-07s
  Max:  5.69e-07s
  Mean: 5.64e-07s +/- 3.64e-09s
```