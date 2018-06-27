class SimpleTextEditor():

    def __init__(self):
        self.prior_string = []
        self.string = ''

    def append(self, word):
        self.prior_string.append(self.string)
        self.string = self.string + word

    def delete(self, k):
        self.prior_string.append(self.string)
        str_length = len(self.string)
        if k > str_length:
            self.string = None
        else:
            self.string = self.string[:(str_length - k)]

    def print(self, k):
        return self.string[k-1]    

    def undo(self):
        if self.prior_string:
            self.string = self.prior_string.pop()


editor = SimpleTextEditor()
number_of_operations = input()
number_of_operations = int(number_of_operations)
res = []
for i in range(number_of_operations):
    req_operation = input().split()
    if req_operation[0] == '1':
        editor.append(req_operation[1])       
    elif req_operation[0] == '2':
        editor.delete(int(req_operation[1]))
    elif req_operation[0] == '3':
        res.append(editor.print(int(req_operation[1])))
    elif req_operation[0] == '4':
        editor.undo()

print('-----------------------')
for r in res:
    print(r)
