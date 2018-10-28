Following is the detailed solution for problem 205:

Consider 9 dies of 4 faces each

Suppose they are rolled together, and the sum comes out to be k
The number of cases having sum k will be the coefficient of x^k in the following expansion:
	exp = (x + x^2 + x^3 + x^4)^9
	
We can simplify this to [x^9 * (1 + x + x^2 + x^3)^9]

By G.P. formula, we get 
	(1 + x + x^2 + x^3) = [(1 - x^4)^9] * [(1 - x)^(-9)]    (say this is (t1 * t2))
	
Coefficient of x^r in (1 - x^4)^9 will be {
	(-1)^k * 9Ck    , if r == 4k
	0               , otherwise
}

We know, coefficient of x^r in (1 - x)^(-n) is given by --> (n+r-1)Cr

Therefore, the coefficient of x^r in exp will be the sum of coefficients of 
x^i from t1 and x^j from t2, such that (i+j) == r

In the code, I have generated the required nCr values in the beginning and stored them in arrays

The code is generalised for Player1 having n dies with 'a' faces each and 
							Player2 having m dies with 'b' faces each
							
Output is the probability of 'a' getting a HIGHER sum than 'b'									
