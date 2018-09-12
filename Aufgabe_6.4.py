from sklearn.datasets import load_iris

# data = load_iris()
# data.target[[10, 25, 50]]
# print(list(data.target))

examples = [["sky", "air", "humid", "wind", "water", "forecast", "attack"],
            ["sunny", "warm", "normal", "strong", "warm", "same", "+"],
            ["sunny", "warm", "high", "strong", "warm", "same", "+"],
            ["rainy", "cold", "high", "strong", "warm", "change", "-"]]


class Tree:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def add_a_branch(self, branch):
        self.branch.append(branch)


# some tests for the tree class
tree = Tree("", [])
branch = Tree("branch", [])
tree.add_a_branch(("label", branch.name))
#print(tree.branch)

'''
def dtLearning(examples, attributes, parent_examples):
    if len(examples) == 0:
        return plurality(parent_examples)
    # elif #same classification?
    elif len(attributes) == 0:
        return plurality(examples)
    else:
        # important_attribute = das wichtigste Attribut
        important_attribute = ""
        tree = Tree(important_attribute, [])
        for each_attribute_value in get_attr_values(important_attribute, examples):
            # exs = Datensätze aus examples bei denen A dem Wert des Elements entspricht
            # subtree = dtLearning(exs, attributes-A, examples)
            # tree = appendBranch(label, subtree)
            tree.add_a_branch(each_attribute_value, "subtree")
        return tree
'''


def get_attr_values(attribute, examples):
    copy_of_examples = examples
    attr_values = []
    i = 0
    for attribute_name in copy_of_examples[0]:
        if attribute_name == attribute:
            copy_of_examples.pop(0)
            for j in range(len(copy_of_examples)):
                if copy_of_examples[j][i] not in attr_values:
                    attr_values.append(copy_of_examples[j][i])
        i += 1
    return attr_values


# test for get_attr_values
print(get_attr_values("sky", examples))



def plurality(examples):
    attribute_values = examples[-1]
    attribute_values.pop(0)
    attribute_values.sort()
    attribute_value_name = attribute_values[0]
    count = 0
    max_count = 0
    value_with_max_count = 'none'
    for i in attribute_values:
        if i == attribute_value_name:
            count += 1
        else:
            if max_count < count:
                max_count = count
                value_with_max_count = i
            count = 0
    return value_with_max_count

# data = [['animals', 'duck', 'duck', 'dog'], ['animals', 'duck', 'duck', 'dog']]
# print(plurality(data))
