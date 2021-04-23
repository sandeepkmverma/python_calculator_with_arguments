import check_value
import sys
import sum_sub
import check_operator
import practice.mul_div

x = check_value.inputNumber(sys.argv[1])
y = check_value.inputNumber(sys.argv[2])
z = check_operator.check_operator(sys.argv[3])

if z=='+':
    sum_value = sum_sub.sum(x,y)
    print("Sum is :", sum_value)


if z=='-':
    sub_value = sum_sub.sub(x,y)
    print("Subtraction is :", sub_value)


if z=='*':
    mul_value = practice.mul_div.mul(x,y)
    print("Multiplication is :", mul_value)


if z=='/':
    div_value = practice.mul_div.div(x,y)
    print("Division is :", int(div_value))



