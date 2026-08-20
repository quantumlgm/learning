package main

import (
	"fmt"
)

func ForLoop() {
	for i := 0; i < 5; i++ {
		fmt.Println(i)
	}

	g := 0
	for g < 5 {
		fmt.Println(g)
		g++
	}

	for {
		fmt.Println("Infinite cycle")
		break
	}

	for range 3 {
		fmt.Println("Hello three times")
	}

	for i:= range 3 {
		fmt.Printf("Hello %d times", i)
	}

	text := "go"
	for i, r := range text {
		fmt.Printf("Индекс: %d, Символ: %c\n", i, r)
	}
}