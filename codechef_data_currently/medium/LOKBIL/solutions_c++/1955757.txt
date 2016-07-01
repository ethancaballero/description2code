#include <iostream>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;

#define INF 100000

int main(int argc, char** argv) {
	int g, f;
	string line, num;

	getline(cin, num);
	istringstream gss(num);
	gss >> g;

	while (g--) {
		getline(cin, num);
		istringstream fss(num);
		fss >> f;

		int graph[101][101];
		for (int i = 1; i <= f; ++i) {
			for (int j = 1; j <= f; ++j) {
				if (i == j) graph[i][j] = 0;
				else graph[i][j] = INF;				
			}
		}

		int j;
		for (int i = 1; i <= f; ++i) {
			getline(cin, line);

			// break into numbers
			istringstream ss(line);
			while (ss >> j) {
				graph[i][j] = 1;
				graph[j][i] = 1;
			}
		}

		for (int k = 1; k <= f; ++k) {
			for (int i = 1; i <= f; ++i) {
				for (int j = 1; j <= f; ++j) {
					graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]);
				}
			}
		}

		// Compute average and find min
		int min_sum = INF;
		int popular = 0;
		for (int i = 1; i <= f; ++i) {
			int sum = 0;

			for (int j = 1; j <= f; ++j) {
				//cout << graph[i][j] << ",";
				if (graph[i][j] != INF) sum += graph[i][j];
			}
			//cout << endl;

			if (sum < min_sum) {
				min_sum = sum;
				popular = i;
			}
		}

		cout << popular << " ";
		double min_avg = (double)min_sum / f;
		cout.setf(ios::fixed,ios::floatfield);
		cout<<setprecision(6)<<min_avg<<endl;

	}

	return 0;
}
