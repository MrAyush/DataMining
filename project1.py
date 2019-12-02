from apyori import apriori

data_set = [['M', 'O', 'N', 'K', 'E', 'Y'], ['D', 'O', 'N', 'K', 'E', 'Y'], ['M', 'A', 'K', 'E'],
           ['M', 'U', 'C', 'K', 'Y'], ['C', 'O', 'O', 'K', 'I', 'E']]
rule = apriori(data_set, min_support=0.6, min_confidence=0.8)
rule_list = list(rule)
print(f'Total Relations found: {len(rule_list)} with 60% minimum support and 80% minimum confidence')

for item in rule_list:
    pair = item[0]
    items = [x for x in pair]
    print(items)
    print(f"Support: {str(item[1])}")
    print(f"Confidence: {str(item[2][0][2])}")
    print(f"Lift: {str(item[2][0][3])}")
    for sub_item in item[2]:
        x = [x for x in sub_item[0]]
        if len(x) is 0:
            continue
        y = [y for y in sub_item[1]]
        print(f'\tRelation: {str(x)} -> {str(y)}')
        print(f'\tConfidence: {str(sub_item[2])}')
        print(f'\tLift: {str(sub_item[3])}\n')
    print("=====================================")
