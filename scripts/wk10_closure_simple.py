# illustrate a closure in python

def outer_function(outer_val):
  print(f'{outer_val = }')

  def inner_function(inner_val):
    # the inner function is the closure - accesses vars from outer function
    print(f'{inner_val = }')
    return outer_val - inner_val

  return inner_function # outer function returns inner function

# create closure object that defines and stores the inner function 
#   along with the outer value
closure = outer_function(100)
print(f'closure object is of type: {type(closure)}')

# execute the inner function by passing a value to the closure object 
closure_result = closure(25)  
print(f'result of inner function run: {closure_result}')