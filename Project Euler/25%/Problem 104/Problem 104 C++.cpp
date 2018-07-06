#include <bits/stdc++.h>
using namespace std;


// in the code below, 
// log(goldenRatio) == 0.208...
// log(root(5)) == 0.349...

int main() {

	long fn2 = 1;
	long fn1 = 1;
	long fn;
	 
	long tailcut = 1000000000;
	 
	int n = 2;
	bool found = false;
	 
	while (!found) {
	    n++;
	    fn = (fn1 + fn2) % tailcut;
	    fn2 = fn1;
	    fn1 = fn;
	 
	    if (IsPandigital(fn)) {
	        double t = (n * 0.20898764024997873 - 0.3494850021680094);
	        if (IsPandigital((long)Math.Pow(10, t - (long)t + 8)))
	            found = true;
	    }
	}
}