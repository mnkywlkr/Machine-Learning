import numpy as np

# data = load_iris()
# data.target[[10, 25, 50]]
# print(list(data.target))

weatherData = [["sky", "air", "humid", "wind", "water", "forecast", "attack"],
               ["sunny", "warm", "normal", "strong", "warm", "same", "+"],
               ["sunny", "warm", "high", "strong", "warm", "same", "+"],
               ["rainy", "cold", "high", "strong", "warm", "change", "-"]]

weatherData2 = [["sky", "sunny", "sunny", "rainy", "sunny", "sunny", "rainy"],
                ["air", "warm", "warm", "cold", "warm", "warm", "warm"],
                ["humid", "normal", "high", "high", "high", "normal", "high"],
                ["wind", "strong", "strong", "strong", "strong", "weak", "strong"],
                ["water", "warm", "warm", "warm", "cool", "warm", "warm"],
                ["forecast", "same", "same", "change", "change", "same", "change"],
                ["attack", "+", "+", "-", "+", "-", "-"]]


class Branch:
    def __init__(self, label):
        self.label = label
        self.tree = None

    def print_branch(self):
        print("--",self.label,"->")
        print(self.tree)


class Tree:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def add_a_branch(self, new_tree,label):
        branch = Branch(label)
        branch.tree = new_tree
        self.branches.append(branch)

    def print_branches(self):
        for b in self.branches:
            print(b.label)

    def print_tree(self):
        print(self.name)
        if len(self.branches) != 0:
            for b in self.branches:
                b.print_branch()



# print(tree.branch)
def copy_2d_array(original_array):
    copy_of_array = []
    for e in original_array:
        column = []
        for a in e:
            column.append(a)
        copy_of_array.append(column)
    return copy_of_array


def dtLearning(examples, attributes, parent_examples):
    if len(examples) == 0:
        return plurality(parent_examples)
    elif is_same_classifications(examples):
        return get_attr_values(get_classification(examples), examples)
    elif len(attributes) == 0:
        return plurality(examples)
    else:
        # important_attribute = das wichtigste Attribut
        important_attribute = getImportanceAttributeName(examples, attributes)
        print("important attribute:", important_attribute)
        tree = Tree(important_attribute)
        attr_value_list = get_attr_values(important_attribute, examples)
        for each_attribute_value in attr_value_list:
            # Datensätze aus examples bei denen A dem Wert des Elements entspricht
            exs = ExampleSetElimination(examples, each_attribute_value, important_attribute)
            subtree = dtLearning(exs, reduce_attr_list(important_attribute, attributes), examples)
            # tree = appendBranch(label, subtree)
            tree.add_a_branch(subtree, each_attribute_value)
           # print("tree's children:", tree.print_branches())
        return tree


def reduce_attr_list(attr, attr_list):
    result = []
    for a in attr_list:
        result.append(a)
    result.remove(attr)
    return result


def get_attr_values_complete_list(attribute, data):
    copy_of_examples = copy_2d_array(data)
    attr_values = []
    for i in copy_of_examples:
        if attribute == i[0]:
            for a in i:
                attr_values.append(a)
    return attr_values


def ExampleSetElimination(examples, attr_value, attr):
    newExamples = copy_2d_array(examples)
    attr_value_list = get_attr_values_complete_list(attr, examples)
    #print("reduced set:",attr_value_list)
    positionList = find_positions(attr_value, attr_value_list)
    for pos in positionList:
        for i, e in enumerate(newExamples):
            e.pop(pos)
    # print(newExamples)
    for ne in newExamples:
        if attr == ne[0]:
            newExamples.remove(ne)
    return newExamples


def find_positions(attr_value, examples):
    positions = []
    for i, e in enumerate(examples):
        if e != attr_value and i != 0:
            positions.append(i)
    # print(positions)
    # return positions.sort(reverse=True)
    # start = len(positions)
    return flipList(positions)


def flipList(list):
    result = []
    max = len(list) - 1
    for n in range((len(list))):
        result.append(list[max - n])
    return result


def updateListAfterPop(list):
    for l in list:
        l -= 1


# test for elimination
# print("before: " + "\n")
# print(str(weatherData2) + "\n")
#ExampleSetElimination(weatherData2, "sunny")


# print("after: " + "\n")
# print(str(weatherData2) + "\n")

def get_attr_values(attribute, data):
    copy_of_examples = copy_2d_array(data)
    attr_values = []
    for i in copy_of_examples:
        if attribute == i[0]:
            for a in i:
                if a not in attr_values:
                    attr_values.append(a)
    if len(attr_values) != 0:
        attr_values.pop(0)
    return attr_values


# test for get_attr_values
# print(get_attr_values("sky", weatherData2))


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


def get_classification(data):
    return data[-1][0]


def is_same_classifications(data):
    return len(get_attr_values(get_classification(data), data)) <= 1


sampledata = [["tries", "result"],
              ["yes", "no"],
              ["alot", "no"],
              ["yes", "no"]]


# print(is_same_classifications(weatherData2))


def importance(attribute_index, examples):
    attribute = examples[attribute_index]

    last_attribute = examples[-1]
    # last_attribute.pop(0)
    # last_attribute.sort()
    positive_and_negative_count = len(last_attribute) - 1
    positive_count = 0

    attribute_positive_value_name = last_attribute[1]
    for index, value in enumerate(last_attribute):
        if index != 0:
            if value == attribute_positive_value_name:
                positive_count += 1

    q = positive_count / positive_and_negative_count
    remainder_result = remainder(attribute, examples, attribute_positive_value_name)
    if remainder_result == None:
        result = b(q)
    else:
        result = b(q) - remainder_result
    return result


def b(q):
    # B(q) = -(q log2 q + (1 - q) log2(1 - q)
    if q != 0:
        b = (q * (np.log(q) / np.log(2)))
        if q != 1:
            b += ((1 - q) * (np.log(1 - q) / np.log(2)))
        b = -b
    else:
        b = 0
    return b


def remainder(attribute, examples, attribute_positive_value_name):
    # attribute.pop(0)
    e_count = len(attribute) - 1
    e1_count = 0

    last_attribute = examples[-1]
    # last_attribute.pop(0)
    p_e1 = 0
    p_e2 = 0

    attribute_value_name = attribute[1]
    for index, value in enumerate(attribute):
        if index != 0:
            if value == attribute_value_name:
                e1_count += 1
                if last_attribute[index] == attribute_positive_value_name:
                    p_e1 += 1
            else:
                if last_attribute[index] == attribute_positive_value_name:
                    p_e2 += 1

    e2_count = e_count - e1_count
    if e1_count > 0:
        q1 = p_e1 / e1_count
    elif e1_count == 0:
        q1 = 0

    if e2_count > 0:
        q2 = p_e2 / e2_count
    elif e2_count == 0:
        q2 = 0

    result = (e1_count / e_count) * b(q1) + (e2_count / e_count) * b(q2)
    return result


def getImportanceAttributeName(examples, attributes):
    # suche das wichtigste Attribut
    ig_max_attribute_name = None
    ig_max = 0
    ig_current = 0
    for attribute_column_index, attribute_column in enumerate(examples):
        if attribute_column_index != (len(examples) - 1):
            ig_current = importance(attribute_column_index, examples)
            #print(ig_current)
            if (ig_current > ig_max):
                ig_max = ig_current
                ig_max_attribute_name = attributes[attribute_column_index]
                # Name des wichtigsten Attributes in ig_max_attribute_name speichern
    return ig_max_attribute_name

    # attributes = ["sky", "air", "humid", "wind", "water", "forecast", "attack"]
    # print(testImportance(weatherData2, attributes))


# TEST

end_result_tree = dtLearning(weatherData2, weatherData[0], [])
i = 1

#dtLearning(weatherData2, weatherData[0], []).print_tree()
