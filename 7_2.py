class Node:
    def __init__(self, name, isFolder, size = 0):
        self.name = name
        self.size = size
        self.isFolder = isFolder
        self.children = []
        self.parent = None

    def addChild(self, childNode):
        print("Adding " + childNode.name)
        self.children.append(childNode)
        childNode.parent = self

    def get_size(self):
        if not self.isFolder:
            return self.size
        else:
            total = 0
            for child in self.children:
                total += child.get_size()
            return total

root = None
current_folder = None

with open('7_input.txt', 'r') as f:
    for line in f:
        splittet_line = line[0:-1].split(" ")
        print(splittet_line)
        is_diretive = splittet_line[0] == "$"
        if is_diretive:
            if splittet_line[1] == "cd":
                if splittet_line[2] == "/":
                    root = Node("/", True)
                    current_folder = root
                elif splittet_line[2] == "..":
                    current_folder = current_folder.parent
                else:
                    current_folder = [node for node in current_folder.children if node.name == splittet_line[2] and node.isFolder][0]
            elif splittet_line[1] == "ls":
                continue
        else:
            if splittet_line[0] == "dir":
                current_folder.addChild(Node(splittet_line[1], True))
            else:
                current_folder.addChild(Node(splittet_line[1], False, int(splittet_line[0])))


total = 70000000
need = 30000000
free = total - root.get_size()
need_to_delete = need - free

choosen_to_delete = root

def check_folder_size(node):
    print(f"checking: {node.name}")
    global choosen_to_delete
    if node.isFolder and need_to_delete <= node.get_size() and node.get_size() < choosen_to_delete.get_size():
        choosen_to_delete = node
    for n in node.children:
        if n.isFolder:
            check_folder_size(n)

check_folder_size(root)

print(choosen_to_delete.get_size())
