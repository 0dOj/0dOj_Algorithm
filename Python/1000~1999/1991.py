tree = {'.':False}
for _ in range(int(input())):
    sub = input().split()
    tree[sub[0]] = (sub[1], sub[2])

result = ''
def preorder(node):
    if tree[node]:
        global result

        result += node
        preorder(tree[node][0])
        preorder(tree[node][1])

def inorder(node):
    if tree[node]:
        global result
        
        inorder(tree[node][0])
        result += node
        inorder(tree[node][1])

def postorder(node):
    if tree[node]:
        global result

        postorder(tree[node][0])
        postorder(tree[node][1])
        result += node

preorder('A')
print(result)

result = ''
inorder('A')
print(result)

result = ''
postorder('A')
print(result)