import numpy as np

attributes = ["sky", "air", "humid", "wind", "water", "forecast", "attack"]

weatherData = [["sky", "sunny", "sunny", "rainy", "sunny", "sunny", "rainy"],
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

    def __str__(self):
        result = "--" + self.label + "-->"
        if type(self.tree) is Tree:
            result += self.tree.name + "\n"
        result += str(self.tree) + "\n"
        return result


class Tree:
    def __init__(self, name):
        self.name = name
        self.branches = []

    def add_a_branch(self, new_tree, label):
        branch = Branch(label)
        branch.tree = new_tree
        self.branches.append(branch)

    def __str__(self):
        result = ""
        for b in self.branches:
            result += self.name
            result += str(b)
        return result


def dtLearning(examples, attributes, parent_examples):
    if len(examples) == 0:
        return plurality(parent_examples)
    elif is_same_classifications(examples):
        return get_attr_values(get_classification(examples), examples)
    elif len(attributes) == 0:
        return plurality(examples)
    else:
        # find the attribute with the highest information gain
        important_attribute = getImportanceAttributeName(examples, attributes)
        # print("important attribute:", important_attribute)
        tree = Tree(important_attribute)
        attr_value_list = get_attr_values(important_attribute, examples)
        for each_attribute_value in attr_value_list:
            # only datasets of example, where important_attribute has the value of each_attribute_value
            exs = ExampleSetElimination(examples, each_attribute_value, important_attribute)
            subtree = dtLearning(exs, reduce_attr_list(important_attribute, attributes), examples)
            tree.add_a_branch(subtree, each_attribute_value)
        return tree

# returns a copy of the given 2d-array
def copy_2d_array(original_array):
    copy_of_array = []
    for e in original_array:
        column = []
        for a in e:
            column.append(a)
        copy_of_array.append(column)
    return copy_of_array

# returns a copy of attr_list without attr
def reduce_attr_list(attr, attr_list):
    result = []
    for a in attr_list:
        result.append(a)
    result.remove(attr)
    return result

#returns the column of the given attribute
def get_attr_values_complete_list(attribute, data):
    copy_of_examples = copy_2d_array(data)
    attr_values = []
    for column in copy_of_examples:
        if attribute == column[0]:
            for a in column:
                attr_values.append(a)
    return attr_values

# returns only the datasets of examples, where attr has the value of attr_value
def ExampleSetElimination(examples, attr_value, attr):
    newExamples = copy_2d_array(examples)
    attr_value_list = get_attr_values_complete_list(attr, examples) # column of the given attribute
    positionList = find_positions(attr_value, attr_value_list) # list of indices of datasets to remove
    # remove datasets
    for pos in positionList:
        for column in newExamples:
            column.pop(pos)
    #print(newExamples)
    for ne in newExamples:
        if attr == ne[0]:
            newExamples.remove(ne)
    return newExamples

# returns a list which contains all indices of values in column that are not the attr_value (in descending order)
def find_positions(attr_value, column):
    positions = []
    for index, value in enumerate(column):
        if value != attr_value and index != 0: # except label
            positions.append(index)
    return flipList(positions)

# returns the list in reversed order
def flipList(list):
    result = []
    max = len(list) - 1
    for n in range((len(list))):
        result.append(list[max - n])
    return result

# Test for ExampleSetElimination
# print("before: " + "\n")
# print(str(weatherData) + "\n")
# exs_test = ExampleSetElimination(weatherData, "sunny", "sky")
# print("after: " + "\n")
# print(str(exs_test) + "\n")

# returns a list which contains all possible values for the given attribute once
def get_attr_values(attribute, data):
    copy_of_examples = copy_2d_array(data)
    attr_values = []
    for column in copy_of_examples:
        if attribute == column[0]:
            for a in column:
                if a not in attr_values:
                    attr_values.append(a)
    if len(attr_values) != 0:
        attr_values.pop(0) #remove label
    return attr_values

# Test for get_attr_values
# print(get_attr_values("sky", weatherData))

# returns the most common output value
def plurality(examples):
    copy_of_examples = copy_2d_array(examples)
    output_values = copy_of_examples[-1] #output values
    output_values.pop(0) #remove label
    output_values.sort()
    attribute_value_name = output_values[0]
    count = 0
    max_count = 0
    value_with_max_count = attribute_value_name
    for current_value in output_values:
        if current_value == attribute_value_name:
            count += 1
        else:
            if max_count < count: #check max_count
               max_count = count
               value_with_max_count = attribute_value_name
            attribute_value_name = current_value #count next value
            count = 1
    if max_count < count: #check max_count
        max_count = count
        value_with_max_count = attribute_value_name
    return value_with_max_count

# Test for plurality
# data = [['animals', 'duck', 'duck', 'dog', 'dog', 'dog'], ['animals', 'duck', 'duck', 'dog', 'dog', 'dog']]
# print(plurality(data))

# returns the label of the output values
def get_classification(data):
    return data[-1][0]

# returns true iff all examples have same classification
def is_same_classifications(data):
    return len(get_attr_values(get_classification(data), data)) <= 1

# returns the information gain of an attribute, given by the index of its column in the set of examples
def importance(attribute_index, examples):
    attribute = examples[attribute_index] #column of the given attribute
    last_attribute = examples[-1] #column of the output vlaues
    positive_and_negative_count = len(last_attribute) - 1 #except label

    # count the positive output value
    positive_count = 0
    attribute_positive_value_name = last_attribute[1] #first output value
    for index, value in enumerate(last_attribute):
        if index != 0: #except label
            if value == attribute_positive_value_name:
                positive_count += 1

    # probability of the positive output value
    q = positive_count / positive_and_negative_count

    remainder_result = remainder(attribute, examples, attribute_positive_value_name)

    if remainder_result is None:
        result = b(q)
    else:
        result = b(q) - remainder_result
    return result

# B(q) = -(q log2(q) + (1 - q) log2(1 - q)
def b(q):
    if q != 0:
        b = (q * (np.log(q) / np.log(2)))
        if q != 1:
            b += ((1 - q) * (np.log(1 - q) / np.log(2)))
        b = -b
    else:
        b = 0
    return b

#calculates remainder function
def remainder(attribute, examples, attribute_positive_value_name):
    last_attribute = examples[-1]  # column of output values
    e_count = len(attribute) - 1 #except label
    e1_count = 0
    p_e1 = 0
    p_e2 = 0

    attribute_value_name = attribute[1] #first value
    for index, value in enumerate(attribute):
        if index != 0: #except label
            if value == attribute_value_name:
                e1_count += 1 #counts the first value
                if last_attribute[index] == attribute_positive_value_name:
                    p_e1 += 1 #counts the positive output value for the first value of the given attribute
            else:
                if last_attribute[index] == attribute_positive_value_name:
                    p_e2 += 1 #counts the positive output value for the second value of the given attribute

    e2_count = e_count - e1_count #count of the second value

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

# returns the label of the attribute with the highest information gain
def getImportanceAttributeName(examples, attributes):
    ig_max_attribute_name = None
    ig_max = 0
    for attribute_column_index, attribute_column in enumerate(examples):
        if attribute_column_index != (len(examples) - 1): #except the output value
            ig_current = importance(attribute_column_index, examples)
            if (ig_current > ig_max):
                ig_max = ig_current
                # store the label of the attribute with the current maximum information gain
                ig_max_attribute_name = attributes[attribute_column_index]
    return ig_max_attribute_name

# TEST
end_result_tree = dtLearning(weatherData, attributes, [])
print(end_result_tree)
