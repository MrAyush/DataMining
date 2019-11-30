from apyori import apriori

data_set = [['M', 'O', 'N', 'K', 'E', 'Y'], ['D', 'O', 'N', 'K', 'E', 'Y'], ['M', 'A', 'K', 'E'],
           ['M', 'U', 'C', 'K', 'Y'], ['C', 'O', 'O', 'K', 'I', 'E']]
rule = apriori(data_set, min_support=0.4, min_confidence=0.2, min_lift=2)
rule_list = list(rule)
print(rule_list[0])
print(len(rule_list))

for item in rule_list:
    pair = item[0]
    items = [x for x in pair]
    print(items)
    print("Support " + str(item[1]))
    print("Confidence: " + str(item[2][0][2]))
    print("Lift: " + str(item[2][0][3]))
    print("=====================================")
