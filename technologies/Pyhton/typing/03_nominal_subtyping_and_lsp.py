type number = int | float


class BaseOrder:
    def __init__(self, procurement_item: str, cost: number) -> None:
        self.procurement_item = procurement_item
        self.cost = cost

    def calculate_total_cost(self):
        return self.cost


class UrgentOrder(BaseOrder):
    def calculate_total_cost(self):
        return self.cost + 1500


class WholesaleOrder(BaseOrder):
    def __init__(self, procurement_item: str, cost: number, quantity: int) -> None:
        super().__init__(procurement_item, cost)
        self.quantity = quantity

    def calculate_total_cost(self) -> number:
        total = self.cost * self.quantity
        if self.quantity > 10:
            total *= 0.9
        return total


def application_module(order: BaseOrder) -> number:
    return order.calculate_total_cost()


def process_corporate_purchase(order: BaseOrder, budget: number) -> number | str:
    total = order.calculate_total_cost()
    if total < budget:
        return budget - total
    return "Not enough money"


if __name__ == "__main__":
    urgent_order = UrgentOrder("Black board", 500)
    print(urgent_order.__dict__)  # {'procurement_item': 'Black board', 'cost': 2000}

    wholesale_order = WholesaleOrder("Notebook", 800, 15)
    print(
        wholesale_order.__dict__
    )  # {'procurement_item': 'Notebook', 'cost': 1350.0, 'quantity': 15}

    budget = 3000

    print(process_corporate_purchase(urgent_order, budget))  # 1000
    print(process_corporate_purchase(wholesale_order, budget))  # Not enough money

    """
    class ErrorOrder: <-- Pyright will highlight this section in red
        pass

    print(process_corporate_purchase(ErrorOrder, budget)) <-- AttributeError: type object 'ErrorOrder' has no attribute 'cost'

    """
