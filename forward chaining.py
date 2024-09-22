class Rule:
    def __init__(self, left, right): 
        self.left = left
        self.right = right

    def follows(self, facts): 
        for fact in self.left: 
            if fact not in facts:
                return False
        return True

    def __str__(self): 
        return " ⋀ ".join(self.left) + " -> " + self.right 
    
    
def locate(intermediates, rules): 
    SAT = set()
    for rule in rules:
        if all(left in intermediates for left in rule.left): 
            SAT.add(rule) 
    return SAT


def forward_chaining(initial_assumption, rules, goal):
    intermediates = set(initial_assumption) 
    while True:
        SAT = locate(intermediates, rules) 
        if not SAT:
            break
        r = SAT.pop() 
        intermediates.add(r.right) 
        rules.remove(r) 
        if goal in intermediates:
            return True 
    return False


def read(filename):
    rules = []
    with open(filename, 'r') as file: 
        for line in file: 
            parts = line.strip().split('->') 
            if len(parts) != 2: 
                continue  
            left = parts[0].strip().split(',') 
            right = parts[1].strip()
            rules.append(Rule(left, right)) 
    return rules 


def read_hypothesis(filename):
    with open(filename, 'r') as file: 
        return file.readline().strip().split(',') 


def main():
    initial_assumption_file = input("Enter the filename containing the initial hypothesis: ")

    rules_file = input("Enter the filename containing the rules: ")

    goal = input("Enter the goal to prove or disprove: ").strip()


    initial_assumption = read_hypothesis(initial_assumption_file)
    rules = read(rules_file)


    result = forward_chaining(initial_assumption, rules, goal)


    if result:
        print("The goal '{}' can be proven from the initial hypotheses.".format(goal))
    else:
        print("The goal '{}' cannot be proven from the initial hypotheses.".format(goal))


if __name__ == "__main__":
    main()


