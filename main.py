import random

def shor_alg(N):
  # a = random.randint(2, N - 1)
  a = 2
  # find period r
  r = find_R()
  if r % 2 == 1:
    return shor_alg(N)
  else:
    f_r_2 = f(r / 2, N)
    if f_r_2 == -1:
      return shor_alg(N)
    else:
      gcd_1 = gcd(f_r_2 + 1, N)
      gcd_2 = gcd(f_r_2 - 1, N)
      return gcd_1, gcd_2

# f(x) = 2^x mod N
def f(x, N):
  return (2 ** x) % N

def find_R():
  return 6

def gcd(m,n):
    if not n:
        return m
    else:
        return gcd(n, m % n)

if __name__=="__main__":
    N = 21
    print(shor_alg(N))