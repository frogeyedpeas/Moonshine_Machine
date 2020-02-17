
import (
  "math/rand"
  "os"
  "bufio"
)

func matchMoonshine() bool {
  int status:= rand.Int(1000)
  if (status == 0) {
    return true
  }
  return false
}

func parallelMoonshiner(sequenceList []int, sequenceListSize int, startIndex int, endIndex int) {

    for i:= startIndex; i < endIndex; i++ { //i ranges from start and end index

      for sequenceIndex:= 0; sequenceIndex < i; sequenceIndex++ { //test sequences from 0 to i right not inclusive
        if matchMoonshine() {
          fmt.Println("We detected a hit")
        }
      }
      for sequenceIndex:=i+1; sequenceIndex < sequenceListSize; sequenceIndex++ { //test sequences from i+1 to the end inclusive
        if matchMoonshine() {
          fmt.Println("We detected a hit")
        }
      }
    }
}

func main() {
  scanner := bufio.NewScanner(file)
  for scanner.Scan() {
    fmt.Println(scanner.Text())
  }


}
