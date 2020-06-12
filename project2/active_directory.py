class Group(object):

	def __init__(self, name):
		self.name = name
		self.groups = []
		self.users = []

	def add_group(self, group):
		self.groups.append(group)

	def add_user(self, user):
		self.users.append(user)

	def get_groups(self):
		return self.groups

	def get_users(self):
		return self.users

	def get_name(self):
		return self.name

def is_user_in_group(user=None, group=None):

	if user is None or len(user) == 0:
		print("Please insert the correct username")
		return
	elif group is None or not isinstance(group, Group):
		print("Please insert the correct group name")
		return
    
	users = group.get_users()
	groups = group.get_groups()

	if user in users:
		return True

	for g in groups:
		if is_user_in_group(user, g):
			return True
			
	return False
    
print("==========Test==========")
parent = Group("Parent")
child = Group("Child")
sub_child1 = Group("Subchild1")
sub_child2 = Group("Subchild2")

parent1 = "Zoe"
parent2 = "Jeff"
child1 = "Judy"
child2 = "Mike"

#parents have access to all children and sub-children
parent.add_user(parent1)
parent.add_user(parent2)
parent.add_group(child)
parent.add_group(sub_child1)
parent.add_group(sub_child2)

#each child only have access to their own directory
sub_child1.add_user(child1)
sub_child2.add_user(child2)

#all the children belongs to the big child directory
child.add_group(sub_child1)
child.add_group(sub_child2)

print("Is Judy in the sub_child1 group?", is_user_in_group("Judy", sub_child1))
print("Is Judy in the sub_child2 group?", is_user_in_group("Judy", sub_child2))
print("Is Judy in the child group?", is_user_in_group("Judy", child))
print("Is Judy in the parent group?", is_user_in_group("Judy", parent))
print("Is Zoe in sub_child1 group?", is_user_in_group("Zoe", sub_child1))

print("Is Tony in parent group?", is_user_in_group("Tony", parent))

print("==========Test Corner Cases==========")
is_user_in_group()
is_user_in_group("", child)
is_user_in_group("Zoe", child1)