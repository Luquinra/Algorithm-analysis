def find_pairs(numbers, target):
    num_set = set(numbers)
    pairs = []
    for num in numbers:
        complement = target - num
        if complement in num_set:
            pairs.append((num, complement))
            num_set.remove(num)  
    return pairs

def main():
    import sys
    args = sys.argv[1:]
    if len(args) < 2:
        print("Usage: python app.py <list_of_numbers> <target_sum>")
        return
    numbers = [int(num) for num in args[0].split(',')]
    target = int(args[1])
    pairs = find_pairs(numbers, target)
    for pair in pairs:
        print("+", pair[0], ",", pair[1])

if __name__ == "__main__":
    main()
