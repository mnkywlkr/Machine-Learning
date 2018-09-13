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


class Tree:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def add_a_branch(self, branch):
        self.branches.append(branch)


# some tests for the tree class
tree = Tree("")
branch_test = Tree("branch")
tree.add_a_branch(branch_test)
# print(tree.branch)

'''
def dtLearning(examples, attributes, parent_examples):
    if len(examples) == 0:
        return plurality(parent_examples)
    # elif #same classification?
        return classification()
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


def get_attr_values(attribute, data):
    copy_of_examples = data
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
# print(get_attr_values("sky", examples))


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
    return data[0][-1]


def is_same_classifications(data):
    return len(get_attr_values(get_classification(data), data)) <= 1


sampledata = [["tries", "result"],
              ["yes", "no"],
              ["alot", "no"],
              ["yes", "no"]]
print(is_same_classifications(sampledata))


def importance(attribute_index, examples):
    attribute = examples[attribute_index]

    last_attribute = examples[-1]
    #last_attribute.pop(0)
    #last_attribute.sort()
    positive_and_negative_count = len(last_attribute)-1
    positive_count = 0

    attribute_positive_value_name = last_attribute[1]
    for index, value in enumerate(last_attribute):
        if index != 0:
            if value == attribute_positive_value_name:
                positive_count +=1

    q = positive_count / positive_and_negative_count
    result = b(q) - remainder(attribute, examples, attribute_positive_value_name)
    return result

def b(q):
    # B(q) = -(q log2 q + (1 - q) log2(1 - q)
    if q != 0:
        b = ( q * (np.log(q) / np.log(2)) )
        if q != 1:
            b +=  ((1 - q) * (np.log(1 - q) / np.log(2)) )
        b = -b
    else:
        b = 0
    return b


def remainder(attribute, examples, attribute_positive_value_name):
    #attribute.pop(0)
    e_count = len(attribute)-1
    e1_count = 0

    last_attribute = examples[-1]
    #last_attribute.pop(0)
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
    q1 = p_e1 / e1_count
    q2 = p_e2 / e2_count

    result = (e1_count / e_count) * b(q1) + ( e2_count / e_count ) * b(q2)
    return result


def testImportance(examples, attributes):
    # suche das wichtigste Attribut
    ig_max_attribute_name = None
    ig_max = 0
    ig_current = 0
    for attribute_column_index, attribute_column in enumerate(examples):
        if attribute_column_index != (len(examples) - 1):
            ig_current = importance(attribute_column_index, examples)
            print(ig_current)
            if (ig_current > ig_max):
                ig_max = ig_current
                ig_max_attribute_name = attributes[attribute_column_index]
                # Name des wichtigsten Attributes in ig_max_attribute_name speichern
    return ig_max

attributes = ["sky", "air", "humid", "wind", "water", "forecast", "attack"]
print(testImportance(weatherData2, attributes))