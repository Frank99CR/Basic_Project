def fibonacci_sequence(num1, num2, counter): 
    if counter <= 10:
     print(num1)
     fibonacci_sum = num1 + num2
     fibonacci_sequence(fibonacci_sum, num1, counter + 1)
        
        
        
fibonacci_sequence(1, 0, 0)
