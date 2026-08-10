package main

import (
	"errors"
	"fmt"
)

func Greeting(name, greet string) string {
	return name + ", " + greet
}

func GreetingDefault(name string) string {
	return Greeting(name, "hello!")
}

func privateFunction() {
	// Function with lower register is private
	// that is one don't called from otherr 
	// package
	fmt.Println("Private!")
}

func Error(a, b int) (int, error) {
	// Can use several data types for 
	// show we return
	if b == 0 {
		return 0, errors.New("cannot divide by zero")
	}
	return a / b, nil
}

func Functions() {
	// Just write function name from other file but same package
	result := GreetingDefault("Ruslan")

	// Write the package name for functions from other package
	fmt.Println(result)
}