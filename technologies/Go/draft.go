package main

import "fmt"

func SomeGreet(name, greet string) string {
	return name + ", " + greet
}

func GreetDefault(name string) string {
	return SomeGreet(name, "hello!")
}

func main() {
	result := GreetDefault("Ruslan")
	fmt.Println(result)
}