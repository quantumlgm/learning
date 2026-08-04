<?php
$var1 = 5;
$var2 = 10;

if($var1 < $var2){
    echo "Var1 is less than Var2";
}

for($i=0; $i<10; $i++){
    echo "Number: ".$i."<br>";
}

while($var1 > 0){
    echo "Var1: ".$var1."<br>";
    $var1--;
}

function isEvenOrOdd($number) {
    if ($number % 2 == 0) {
        return "even";
    } else {
        return "odd";
    }
}

$numbers = array(1, 2, 3, 4, 5);
foreach ($numbers as $num) {
    echo "Number ".$num." is ".isEvenOrOdd($num)."<br>";
}

function factorial($number) {
    if ($number == 0) {
        return 1;
    } else {
        return $number * factorial($number - 1);
    }
}

$factorials = array(0, 1, 2, 3, 4, 5);
foreach ($factorials as $num) {
    echo "Factorial of ".$num." is ".factorial($num)."<br>";
}
?>