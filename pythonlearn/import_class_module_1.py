from admin import Admin


# Create an instance of Admin, and call your method.


administrator = Admin('kuljot biring', 99999, 'california')
administrator.describe_user()
administrator_privileges = ['can add post', 'can delete post', 'can ban user']

administrator.privileges.privileges = administrator_privileges

administrator.privileges.show_privileges()
