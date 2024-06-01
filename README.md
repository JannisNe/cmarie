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
testing cython
running ...
 10000 x 5 times ....
------------ cython ------------ 
  Result: 0.2500000009313226
  Min:  3.05e-05s
  Max:  3.11e-05s
  Mean: 3.08e-05s +/- 2.18e-07s


testing python
running ...
 100000 x 5 times ....
------------ python ------------ 
  Result: 0.25
  Min:  3.74e-06s
  Max:  3.75e-06s
  Mean: 3.75e-06s +/- 3.17e-09s


testing c
running ...
 5000 x 5 times ....
------------ c ------------ 
  Result: 0.2500000002328344
  Min:  6.79e-05s
  Max:  6.81e-05s
  Mean: 6.80e-05s +/- 5.99e-08s
```