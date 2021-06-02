class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        inventory.append(0)
        inventory.sort(reverse=True)
        i, width, sold, amount = 0, 0, 0, 0
        while orders > 0:
            width += 1
            sold = min(orders, width * (inventory[i] - inventory[i+1]))
            whole, remainder = divmod(sold, width)
            # amount = width * sum of each sequence + remainder * (inventory[i]-whole)
            amount += width * ((inventory[i] + inventory[i] - whole + 1) * whole // 2) + remainder * (inventory[i] - whole)
            orders -= sold
            i += 1
        return amount % (10 ** 9 + 7)
