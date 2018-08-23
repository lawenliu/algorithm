// main.go
// This test is used to show how to use python code into golang code.
// You can refer the sample here: https://studygolang.com/articles/12822?fr=sidebar
// Also you can check more functions usage here: https://godoc.org/github.com/sbinet/go-python
// How to run the program? you need build python code to .pyc file and then build and run this golang code
package main

import (
    "fmt"
    "github.com/sbinet/go-python"
)

var (
    PyStr = python.PyString_FromString
    GoStr = python.PyString_AS_STRING
)

func init() {
    err := python.Initialize()
    //fmt.Println("init")
    if err != nil {
        panic(err.Error())
    }

    defer python.Finalize()
}

func main() {
    python.Initialize()
    defer python.Finalize()

    //InsertBeforeSysPath("/root/anaconda3/lib/python3.6/site-packages")
    fooModule := ImportModule("/root/go_python_test/cplus", "hello")
    if fooModule == nil {
        panic("Error importing module")
    }

    helloFunc := fooModule.GetAttrString("b")
    if helloFunc == nil {
        panic("Error importing function")
    }

    // The Python function takes no params but when using the C api
    // we're required to send (empty) *args and **kwargs anyways.
    bArgs := python.PyTuple_New(1)
    python.PyTuple_SetItem(bArgs, 0, PyStr("xixi"))
    res := helloFunc.Call(bArgs, python.Py_None)
    fmt.Println(GoStr(res))
}

// InsertBeforeSysPath will add given dir to python import path
func InsertBeforeSysPath(p string) string {
    sysModule := python.PyImport_ImportModule("sys")
    path := sysModule.GetAttrString("path")
    python.PyList_Insert(path, 0, PyStr(p))
    return GoStr(path.Repr())
}

// ImportModule will import python module from given directory
func ImportModule(dir, name string) *python.PyObject {
    sysModule := python.PyImport_ImportModule("sys") // import sys
    path := sysModule.GetAttrString("path")                    // path = sys.path
    python.PyList_Insert(path, 0, PyStr(dir))                     // path.insert(0, dir)
    return python.PyImport_ImportModule(name)            // return __import__(name)
}

