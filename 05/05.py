class PrinterConfig:
    def __init__(self, rules, page_orders):
        self.rules = rules
        self.parsed_rules = {}
        for rule in self.rules:
            before,after = rule.split('|')
            self.parsed_rules.setdefault(int(after),[]).append(int(before))
        # print(self.parsed_rules)

        self.page_orders = []
        for order in page_orders:
            new_order = []
            for page in order.split(','):
                new_order.append(int(page))
            self.page_orders.append(new_order)
    
    def check_ordering(self, page_order, should_print = False):
        # print(page_order)
        for i in range(len(page_order)):
            page = page_order[i]
            page_rule = self.parsed_rules.get(page,[])
            for after_page in page_order[i+1:]:
                # print(f'checking for {after_page} in {page_rule}: {after_page in page_rule}')
                if after_page in page_rule:
                    if(should_print):
                        print(f'Page {after_page} must come before {page}')
                    return False
        
        return True
    
    def correct_ordering(self, page_order):
        # print(page_order)
        max_iter = len(page_order) * len(page_order) * len(page_order)
        new_order = page_order
        iter = 0
        while not self.check_ordering(new_order):
            iter +=1
            if iter >= max_iter:
                return None
            temp_order = []
            for i in range(len(new_order)):
                page = new_order[i]
                if page in temp_order:
                    continue
                page_rule = self.parsed_rules.get(page,[])
                for after_page in new_order[i+1:]:
                    if after_page in page_rule and not after_page in temp_order:
                        temp_order.append(after_page)
                temp_order.append(page)
            if new_order == temp_order:
                print(page_order)
                print(new_order)
                print(temp_order)
                print(iter)
                self.check_ordering(new_order, True)
                return None
            new_order = temp_order
        return new_order
            



def read_input():
    rules = []
    page_orders = []
    for line in open('input.txt', 'r'):
        line = line.rstrip()
        if "|" in line:
            # It's a rule
            rules.append(line)
        if "," in line:
            page_orders.append(line)
            # It's a page_order
    
    return PrinterConfig(rules, page_orders)

def part1():
    config = read_input()
    sum = 0
    for order in config.page_orders:
        if config.check_ordering(order):
            sum+= order[len(order) // 2]
    
    print(f'Part1={sum}')

def part2():
    config = read_input()
    sum = 0
    for order in config.page_orders:
        if not config.check_ordering(order):
            new_order = config.correct_ordering(order)
            if new_order is not None:
                sum += new_order[len(new_order) // 2]
    print(f'Part2={sum}')

part1()
part2()