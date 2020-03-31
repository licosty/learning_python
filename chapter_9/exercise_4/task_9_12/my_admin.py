''' Страница упражнения - 182 '''

# 9-12
from admin import Admin
admin = Admin('admin', 'admin', ["add user", "del user", "change user"])
admin.privileges.show_privileges()