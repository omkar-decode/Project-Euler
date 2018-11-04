
Consider N to be the side length of the lamina & 
	k is the 'thickness' of the lamina

Eg: in the first instance given in the problem, N=6 & k=2
	in the second instance, N=9 & k=1

if we have to make a lamina with T tiles, we can derive the expression
	(4 * k * (N-k)) = T

Therefore, T must be a multiple of 4 and the number of laminae for a given T 
	will be the number of factors of (T/4) which are less than or equal to sqrt(T/4)

This can be written as:
	[number of laminae = ((Total number of factors of T/4) + 1) // 2]

The above expression takes care for both odd and even T/4

Note: since we are considering laminae with a hole, all the cases where the lamina has no hole must be ignored
		the number to be subtracted is simply the number of perfect squares from 1 to 250,000 (inclusive)