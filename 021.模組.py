# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                   #
#                             Module                                #
#                                                                   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
import support
support.log('skye', 18)

from support import log
log('skye', 18)

from sys import path
log(path)

# __name__ === '__main__' => 表示本身為主運行
# __name__ === '__file_name__ => 表示為加載的模組
print(__name__)
support.test()

# dir 可以看到這個物件下的所有屬性和函數名
print(dir(support))

print(dir(log))

print('----------------------')
print(dir())

print('----------------------')
import my_module.fmt.core
my_module.fmt.core.fmt_core()

# from my_module.fmt.core import fmt_core
# fmt_core()

# from my_module.fmt.core import *
# fmt_core()

# from my_module.fmt import core
# core.fmt_core()

# from my_module.fmt import *
# core.fmt_core()
# core2.fmt_core2()

# from my_module.fmt import core, core2
# core.fmt_core();
# core2.fmt_core2()