package main

import (
	"fmt"
	"strconv"
	"unicode/utf8"
)

func Strings() {
	hello := "Hello"
	world := " World!"

	fmt.Println(hello + world) // Hello World!

	fmt.Println(string(65))
	// It doesn't work because Go 
	// does not convert numbers to strings.
	// For that better use this:

	count := 10
	msg := "You need to try it " + strconv.Itoa(count) + "times "
	fmt.Println(msg)

	// Or approach for float numbers
	countFloat := 7.6
	msg = "Your score is " + strconv.FormatFloat(countFloat, 'f', 2, 64)
	fmt.Println(msg)

	// For interpolation
	name := "Michael"
	msg = fmt.Sprintf("Hello %s!", name)

	// String lenght (Counts with spaces).
	// Golang have byte consequence instead of
	// symbols. In that Cyrillic, Latin, and 
	// emoji have different lengths.
	fmt.Println(len("Beautiful")) // 9
	fmt.Println(len("Кириллица")) // 18
	fmt.Println(len("123456789")) // 9
	fmt.Println(len("😀")) // 4

	// So, if we want to count difinetly symbols,
	// we need to use this:
	fmt.Println(utf8.RuneCountInString("Beautiful")) // 9
	fmt.Println(utf8.RuneCountInString("Кириллица")) // 9
	fmt.Println(utf8.RuneCountInString("123456789")) // 9
	fmt.Println(utf8.RuneCountInString("😀")) // 1

	// And for example look at this:
	runes := []rune("Hello")
	fmt.Println(runes[1]) // 101
}