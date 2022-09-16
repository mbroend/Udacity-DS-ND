## Importing the entire module2
from package1 import module2
module2.module2func()
module2.newmodule2func()

# Importing specific class specified in __init__.py
from package2 import Class1
new_class  = Class1
print(new_class.x)

# importing all of package2
import package2 as p2

try:
    p2.module3.module3func()
except:
    print('If the above fails - why?')


from package2 import module3, module4

module3.module3func()


