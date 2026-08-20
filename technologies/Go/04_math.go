package main

import "fmt"

func MathBasic() {
	x := 10
	y := 5

	// x + y = 15
	// x - y = 5
	// x * y = 50
	// x / y = 2

	x += x  // 20
	x -= 10 // 10
	x /= y  // 2

	res := float64(10) / float64(20)
	fmt.Println(res) // 0.5
}