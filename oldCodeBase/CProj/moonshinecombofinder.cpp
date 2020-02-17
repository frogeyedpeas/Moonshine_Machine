#include <string>
#include <iostream>
#include <fstream>
#include <vector>
#include <cstring>
#include <gmpxx.h>


using namespace std;
//A canonical subset sum implementation
bool subsetSum(long long int targetSum, vector<long long int> targetArray , int max) {
  if (max < 1) {
    return false;
  }

  if (targetSum==0) {
    return true;
  }
  if (targetSum < 0) {
    return false;
  }

  bool included = subsetSum(targetSum - targetArray[max - 1], targetArray, max - 1);
  bool discluded = subsetSum(targetSum, targetArray, max - 1);

  return included || discluded;

}

bool IsListExpressed(vector<long long int> targetList, vector<long long int> sourceList, int bound) {
  int i = 0;
  while (i < bound) {
    if (!subsetSum(targetList[i], sourceList, bound)) {
       return false;
    }
    i++;
  }
  return true;
}

bool validityChecker(vector<long long int> integerSequence) {
  // These are our conditions for minimum gap between elements and minimum length of number sequences
  int MINGAP = 50;
  int MINLENGTH = 10;
  int prev = -MINGAP;
  int arraySize = integerSequence.size();

  if (arraySize < MINLENGTH) {
    return false;
  }

  int i = 0;
  while (i < arraySize) {
    if (integerSequence[i] < prev + MINGAP) {
      return false;
    }
    prev = integerSequence[i];
    i++;
  }

  return true;

}


vector<vector<long long int> > aggregatorProcessor(vector<vector<long long int> > OEISLists, int sequenceCount) {


  vector<vector<long long int> > coincidences;
  // now we need to basically consider every pair of possible lists in OEISLists, filter for compatiblity and then check
  // for summability

  int leftIndex = 0;
  int rightIndex;
  int scanningIndex;
  int leftArraySize;
  int rightArraySize;
  int bound = 10;

  int leftMax = 10000; //should be sequenceCount
  //For each I
  // If fails condition then continue
  // Condition is a loop
  while (leftIndex < leftMax) { //While
    cout << leftIndex << "\n";
    scanningIndex = 0;
    rightIndex = 0;
    //check that our leftIndex is at an admissible location, else push it along

    if (!validityChecker(OEISLists[leftIndex])) {
      leftIndex++;
      continue;
    }

    //if we reach this point then we have a valid left sequence, now we need a right sequence.

    rightIndex = leftIndex + 1;

    while (rightIndex < sequenceCount) {
      // cout << rightIndex << "\n";
      if (!validityChecker(OEISLists[rightIndex])) {
        rightIndex++;
        continue;
      }

      // at this point we have a valid left and right index.
      // now we test for SubSetSummability.

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

  string line;

  char* token;

  vector<vector<long long int> > integerSequences;

  ifstream sequenceFile ("sequenceFile.txt");

  int exceptor;

  bool addflag;

  int debugcounter = 0;

  if (sequenceFile.is_open()) {


    while (getline(sequenceFile, line)) {

      cout << debugcounter << "\n";
      debugcounter++;
      //line at this point is filled with a line
      addflag = true;
      //cout << line << "\n \n";
      vector<long long int> temp;
      char cline[line.size()+1];
      strcpy(cline, line.c_str());
      token = strtok(cline, " ");
      while (token != NULL) {
        exceptor = -1;
        try {

          exceptor = strlen(token);
          if (exceptor > 10) {
            throw exceptor;
          }
          // cout << token;
          temp.push_back(stoll(token, nullptr, 10));
        }
        catch (int exceptor) {
          // cout << "BIG f'n number found\n";
          addflag = false;
          break;
        }
        token = strtok(NULL, " ");
      }
      if (addflag) {
        integerSequences.push_back(temp);
      }

    }
    sequenceFile.close();
  }

  else {
    cout << "Unable to Open Input File!";
  }

  vector<vector<long long int> > coincidences = aggregatorProcessor(integerSequences, integerSequences.size());

  int coincidenceSize = coincidences.size();
  int i = 0;
  int j;
  int individualCoincidenceSize;
  ofstream outputFile ("cprocessedoutput");

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
