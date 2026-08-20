package main

import (
	"strings"
)


func ModifySpaces(s, mode string) string {
	switch mode {
		case "dash":
			return strings.ReplaceAll(s, " ", "-")
		case "underscore":
			return strings.ReplaceAll(s, " ", "_")
		default:
			return strings.ReplaceAll(s, " ", "*")
	}	
}
