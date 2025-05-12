#include <fstream>
#include <iostream>
#include <random>


using namespace std;

string random_sequence() {

    mt19937 gen(random_device{}());

    uniform_int_distribution<int> distribution(0,1);

    string sequence;

    for (size_t i = 0; i < 128; ++i) {

        sequence += to_string(distribution(gen));

    }

    return sequence;

}

void save_file(const string& filename, const string& sequence) {

    ofstream file(filename);

    file << sequence;

}

int main() {

    string rndmSequence = random_sequence();
    save_file('cpp_subs.txt',rndmSequence)

}
