package main

//This is going to attempt to read and write to a file now

import (
  "fmt"
  "os"
  "sync"
  "bufio"
  "math/big"
)


func check(e error) {
    if e != nil {
        panic(e)
    }
}

func fileCreator(fileName string, waitGroup *sync.WaitGroup) {

  defer waitGroup.Done()
  f,err := os.Create(fileName)
  check(err)
  defer f.Close()
  w := bufio.NewWriter(f)
  n4, err := w.WriteString("This is a new file " + fileName)
  fmt.Println(n4)
  fmt.Println(err)
  w.Flush()
}

func sharedRead(fileName string, waitGroup *sync.WaitGroup) {

    defer waitGroup.Done()
    f,err := os.Open(fileName)
    check(err)
    defer f.Close()

    lineScanner := bufio.NewScanner(f)
    for lineScanner.Scan() {
      fmt.Println(lineScanner.Text())
    }
}

func Operate() {

  //reading an integer
  age := new(big.Int)
  var ageString string
  fmt.Println("What is your age?")
  fmt.Scan(&ageString)


  age, ok := age.SetString(ageString, 10)

  if !ok {
    fmt.Println("OMG something bad happened")
    return
  }
  fmt.Println(age, " is but a number")

}

func main() {

    // define a waitGroup WaitGroup and test shared reading

    


    waitGroup.Add(3)

    fmt.Println("Now we commence waiting")
    fmt.Println("Now we are done")
}
