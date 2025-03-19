#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cmath>

using namespace std;

double round_2_places(double var) {
    return round(var * 100) / 100;
}

void calcular_troco(vector<double>& cambio, double troco_devido) {
    sort(cambio.begin(), cambio.end(), greater<double>());

    double troco_pago = 0;
    map<double, int> troco_map;
    for(double i: cambio) {
        troco_map[i] = 0;
    }   

    while(troco_pago < troco_devido) {
        for(double c: cambio) {
            if(round_2_places(troco_pago + c) <= troco_devido) {
                troco_map[c]++;
                troco_pago = round_2_places(troco_pago + c);
            }
        }
    }

    cout << troco_pago << endl;
    for(double c: cambio) {
        cout << c << "->" << troco_map[c] << endl;
    }
}

int main() {
    vector<double> cambio = {0.01, 0.03, 0.04};
    double troco_devido = 0.06;

    calcular_troco(cambio, troco_devido);

    return 0;

}