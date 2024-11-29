#include <iostream>
#include <iomanip>
#include <math.h>


using namespace std;

string bin(unsigned int num) {
	string s = "";

	while (num > 0) {
		s = (num & 1 ? "1" : "0") + s;
		num >>= 1;
	}
	return s;
}

string zfill(string s, int size) {
	int p = size - s.length();
	for (int i = 0; i < p; i++) {
		s = "0" + s;
	}
	return s;
}

string bits(string s) {
	string r = "";

	for (int i = 1; i <= s.length(); i++) {
		r += s[i - 1];
		if (i % 4 == 0) {
			r += " ";
		}
	}
	return r;
}




int main() {
	int x;
	cin >> x;
	unsigned int c = x;
	cout << c;
	

}


