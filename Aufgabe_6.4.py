from sklearn.datasets import load_iris

# data = load_iris()
# data.target[[10, 25, 50]]
# print(list(data.target))

"""
def dtLearning (examples, attributes, parent_examples):
    if len(examples) == 0:
        return plurality(parent_examples)
    elif #same classification?
    elif len(attributes) == 0:
        return plurality(examples)
    else
        #suche das wichtigste Attribut
        #tree = neuen Baum erzeugen
        # für alle Elemente in A
            #exs = Datensätze aus examples bei denen A dem Wert des Elements entspricht
            #subtree = dtLearning(exs, attributes-A, examples)
            #tree = appendBranch(label, subtree)
        #return tree

"""


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


data = [['animals', 'duck', 'duck', 'dog'], ['animals', 'duck', 'duck', 'dog']]
print(plurality(data))
