class Machine:
    ingredient = ["water", "milk", "coffee beans", "disposable cups", "money"]
    metrics = ["ml", "ml", "grams ", "pieces"]
    in_machine_info = [400, 540, 120, 9, 550]
    menu_names = ['espresso', 'latte', 'cappuccino']
    menu = [[250, 0, 16, 1, -4], [350, 75, 20, 1, -7], [200, 100, 12, 1, -6]]

    def enough_for_order(self, order):
        for n in range(len(self.ingredient)):
            if self.in_machine_info[n] < order[n]:
                return self.ingredient[n]
        return ''

    def info(self):
        print(f"\nThe coffee machine has:")
        for i in range(len(self.ingredient)):
            print(str(self.in_machine_info[i]) + " of " + self.ingredient[i])

    def action(self):
        while True:
            print("\nWrite action (buy, fill, take, remaining, exit):")
            action = input()
            if action == "buy":
                self.buy()
            elif action == "fill":
                self.fill()
            elif action == "take":
                self.take()
            elif action == "remaining":
                self.info()
            elif action == "exit":
                break

    def buy(self):
        s = "\nWhat do you want to buy? " + ("%s, " * len(self.menu_names)) + "back - to main menu:"
        print(s % tuple([(str(n) + " - " + self.menu_names[n - 1]) for n in range(1, len(self.menu_names) + 1)]))
        client_input = input()
        if client_input == "back":
            return
        order = int(client_input) - 1
        check_result = self.enough_for_order(self.menu[order])
        if (len(self.menu) > order >= 0) and len(check_result) < 2:
            print("I have enough resources, making you a coffee!")
            for d in range(len(self.in_machine_info)):
                self.in_machine_info[d] -= self.menu[order][d]
        else:
            print(f"Sorry, not enough {check_result}!")

    def fill(self):
        for i in range(len(self.in_machine_info) - 1):
            print(f"Write how many {self.metrics[i]} of {self.ingredient[i]} do you want to add:")
            self.in_machine_info[i] += int(input())

    def take(self):
        print(f"I gave you ${self.in_machine_info[4]}")
        self.in_machine_info[4] = 0


m = Machine()
m.action()
