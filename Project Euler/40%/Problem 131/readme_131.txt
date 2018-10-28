We need to find some kind of relation between p and n

Let us assume that for some positive k,
	(n^3 + (n^2)p) = (n + k)^3		----->  (1)

On simplifying (1), we get 
	p = 3k + ((3(k^2))/n) + ((k^3)/(n^2))		(say this is (t1 + t2 + t3))	----->	(2)

Let -->		k = Product (p(i)^a(i))			----->	(3)
									where Product() means 'product over all' and
									p(i) is the i'th prime in k's prime factorisation, having exponent a(i)


Now, consider some prime p(j) which IS a factor of k
Since p in (2) is prime, p(j) is not a factor of p

We see that exponent of p(j) will be non-zero in t1
Therefore, we can infer that the exponent of p(j) must be 0 in either t2 or t3

	Case 1: p(j) is not a factor of t2
			Since k is squared in the numerator, n must have (p(j)^(2a(j))) as a factor

			But this would result in p(j) having a higher exponent in the denominator of t3 (4a(j)) than in its numerator (3a(j))
			Since p is an integer, t3 must be an integer

			Therefore this case is not possible

	Case 2: p(j) is not a factor of t3
			Since k is cubed in the numerator, n must have (p(j)^((3/2)a(j))) as a factor

			This case is fine, since it gives a positive exponent of p(j) in t2

	Since Case 2 holds for every p(j) in k, n would be of the following form
		
		n = Product (p(i)^((3/2)a(i)))		----->	(4)


From (3) and (4), we see that 
	n^2 = k^3	=>	k = n^(2/3)			----->	(5)


Substituting (5) in (2), we get
	p = 3(n^(2/3)) + 3(n^(1/3)) + 1


Let	-->		x = n^(1/3)	 =>	 n = x^3			----->	(6)


Therefore, the equation becomes
	p = 3(x^2) + 3x + 1


So, every prime which satisfies the given condition	should also be of the above form

To get a list of primes satisfying the given condition, we can substitute different integer values for x,
	and if the resultant p is a prime, it would satisfy the given condition for n = x^3 and k = x^2

So, we simply need to iterate over x, starting from x=1, and stop when p exceeds one million
For every value of x which gives a prime p, we increment a counter (initialised to 0)

Final value of the counter is the required answer				
