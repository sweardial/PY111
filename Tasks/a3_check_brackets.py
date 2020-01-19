
string = ""

def check_brackets(brackets_row: str) -> bool:
	stack = []
	string = brackets_row
	if len(string)% 2 != 0:
		return False

	for i in string:
		if i == '(':
			stack.append(i)
		if i == ')':
			stack.pop()
	if stack:
		return False
	else:
		return True





