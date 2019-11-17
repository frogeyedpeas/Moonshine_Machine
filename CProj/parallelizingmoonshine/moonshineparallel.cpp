#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <gmpxx.h>

using namespace std;

//globally defined 0
mpz_t ZERO;
mpz_t MINGAP;
//A canonical subset sum implementation
bool subsetSum(mpz_class targetSum, vector<mpz_class> targetArray , int max) {
  if (max < 1) {
    return false;
  }

  int are_we_there = mpz_cmp(targetSum.get_mpz_t(), ZERO);

  if (are_we_there > 0) {

    mpz_class potential;
    mpz_sub(potential.get_mpz_t(), targetSum.get_mpz_t(), targetArray[max - 1].get_mpz_t());
    bool included = subsetSum(potential, targetArray, max - 1);
    bool discluded = subsetSum(targetSum, targetArray, max - 1);

    return included || discluded;

  }

  if (are_we_there == 0) {
    return true;
  }

  if (are_we_there < 0) {
    return false;
  }

  else {
    cout << "HOLY SHIT ITS WEIRD" << "\n";
    return false;
  }

}

bool IsListExpressed(vector<mpz_class> targetList, vector<mpz_class> sourceList, int bound) {
  int i = 0;
  while (i < bound) {
    if (!subsetSum(targetList[i], sourceList, bound)) {
       return false;
    }
    i++;
  }
  return true;
}


vector<vector<mpz_class> > aggregatorProcessor(vector<vector<mpz_class> > OEISLists, int sequenceCount, int startbound, int endbound) {

  vector<vector<mpz_class> > coincidences;
  // now we need to basically consider every pair of possible lists in OEISLists, filter for compatiblity and then check
  // for summability

  int leftIndex = startbound;
  int rightIndex;
  int scanningIndex;
  int leftArraySize;
  int rightArraySize;
  int bound = 10;

  int leftMax = endbound; //should be sequenceCount
  int rightMax = sequenceCount;

  // Condition is a loop
  while (leftIndex < leftMax) { //While
    cout << leftIndex << "\n";


    rightIndex = leftIndex + 1;

    while (rightIndex < rightMax) {

      if (IsListExpressed(OEISLists[leftIndex], OEISLists[rightIndex], bound)) {
        coincidences.push_back(OEISLists[leftIndex]);
        coincidences.push_back(OEISLists[rightIndex]);
      }

      if (IsListExpressed(OEISLists[rightIndex], OEISLists[leftIndex], bound)) {
        coincidences.push_back(OEISLists[rightIndex]);
        coincidences.push_back(OEISLists[leftIndex]);
      }

      rightIndex++;

    }

    leftIndex++;

  }

  return coincidences;

}



int main(int argc, char* argv[]) {




  mpz_set_str(ZERO, "0",10); //get 0 set up
  mpz_set_str(MINGAP, "50", 10);
  int MINLENGTH = 10;
  string line;
  char* token;
  vector<vector<mpz_class> > integerSequences;
  ifstream sequenceFile ("sequenceFile.txt");
  int exceptor;
  bool addflag;
  int debugcounter = 0;
  int size_tracker = 0;
  mpz_class prev;

  long long int leftBound = stoll(argv[1], nullptr, 10);
  long long int rightBound = stoll(argv[2], nullptr, 10);

  if (sequenceFile.is_open()) {


    while (getline(sequenceFile, line)) {

      //our logic for validity checking happens here too
      mpz_neg(prev.get_mpz_t(), MINGAP); //prev = -MINGAP
      cout << debugcounter << "\n";
      debugcounter++;
      //line at this point is filled with a line
      addflag = true;
      //cout << line << "\n \n";
      vector<mpz_class> temp;
      mpz_class holder;
      char cline[line.size()+1];
      strcpy(cline, line.c_str());

      size_tracker = 0;
      token = strtok(cline, " ");
      while (token != NULL) {
        mpz_add(prev.get_mpz_t(), prev.get_mpz_t(), MINGAP);

        mpz_set_str(holder.get_mpz_t(), token, 10); //attempt to convert

        if (mpz_cmp(prev.get_mpz_t(), holder.get_mpz_t()) > 0) {

          addflag = false;
          break;

        }

        temp.push_back(holder); //dump it into the vector
        token = strtok(NULL, " ");
        size_tracker++;

        mpz_set(prev.get_mpz_t(), holder.get_mpz_t()); //update previous to the current element, ensures a gap of MINGAP between terms
      }
      if (addflag && size_tracker > MINLENGTH) {
        integerSequences.push_back(temp);
      }
    }
    sequenceFile.close();
  }

  else {
    cout << "Unable to Open Input File!";
  }

  cout << integerSequences.size() << "\n";
  vector<vector<mpz_class> > coincidences = aggregatorProcessor(integerSequences, integerSequences.size(), leftBound, rightBound);
  // vector<vector<mpz_class> > coincidences = integerSequences;
  int coincidenceSize = coincidences.size();
  int i = 0;
  int j;
  int individualCoincidenceSize;
  // const char* namestring = argv
  ofstream outputFile (argv[3]);

  if (outputFile.is_open()) {

    while (i < coincidenceSize) {
      j = 0;
      individualCoincidenceSize = coincidences[i].size();
      while (j < individualCoincidenceSize) {
        outputFile << coincidences[i][j] << " ";
        j++;
      }
      outputFile << "\n";
      i++;
    }
  }
  else {
    cout << "Unable to Open Output File!";
  }
  return 0;

}
