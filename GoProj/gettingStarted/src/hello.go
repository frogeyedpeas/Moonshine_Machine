package main

//This is going to attempt to read and write to a file now

import (
  "fmt"
  "os"
  "sync"
  "bufio"
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

func sharedRead(fileName string) {

    f,err := os.Open(fileName)
    check(err)
    defer f.Close()

    lineScanner := bufio.NewScanner(f)
    for line in lineScanner.Scan() {
      fmt.Println(line)
    }
}

func main() {

    /* var waitGroup sync.WaitGroup
    go fileCreator("test", &waitGroup)
    go fileCreator("best", &waitGroup)
    go fileCreator("west", &waitGroup)
    waitGroup.Add(3)
    waitGroup.Wait()

    */


    sharedRead("testfile")

    fmt.Println("Now we commence waiting")
    fmt.Println("Now we are done")
}
