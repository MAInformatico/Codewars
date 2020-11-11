def tree_by_levels(node):
    result, queue = [], [node]
    while queue:
        currentValue = queue.pop(0)
        if currentValue is not None:
            result.append(currentValue.value)
            queue += [currentValue.left,currentValue.right]
    return result if not node is None else []
