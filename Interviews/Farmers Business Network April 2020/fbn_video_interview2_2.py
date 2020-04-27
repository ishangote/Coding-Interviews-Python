"""
Scenario: you work in a warehouse, about to ship pallets on a fleet of trucks to deliver to various farmers today.
How can you load the pallets to use the minimum number of trucks, while not splitting farmers orders?

                   _______________________________________________________
                  |                                                      |
             /    |                                                      |
            /---, |                                                      |
       -----# ==| |                                                      |
       | :) # ==| |                                                      |
  -----'----#   | |______________________________________________________|
  |)___()  '#   |______====____   \___________________________________|
 [_/,-,\"--"------ //,-,  ,-,\\\   |/             //,-,  ,-,  ,-,\\ __#
   ( 0 )|===******||( 0 )( 0 )||-  o              '( 0 )( 0 )( 0 )||
----'-'--------------'-'--'-'-----------------------'-'--'-'--'-'--------------


 .-------.=======Oo, .---------------------------------------------------.    ___
{|----. ||     .-- |?| x # # # x x                                       |  --
||    | ||    |    |7| x # # # @ x                                       |    ----
||    | ||    |    |{| x x # # @ x                                       | ____
{|----' ||     `-- |V| x x # # @ x                                       |    __
 '-------'=========" '---------------------------------------------------'  ---

# Decide where to put each order for the minimum number of trucks.
# constraint: Do not split a customer's order onto multiple trucks.
# if we have time: create a loading map/printout function to fill the truck so that all a customer's pallets are next to each other. This makes it easy for delivery unloading.

one row -> 4 pallets possible

          0.  1.  2.  3
trucks = [22, 30, 26, 40]
          0   7    6   20

          0.  1.  2.  3
trucks = [22, 26, 30, 40]   
          12  26  30  40
          0   26  30  40 
          0.  6.  30. 40
          0. 6.   10. 40
          0. 6. 0.    40
          0  0   6.  40
          0  0  6.  19
          
Pseudo:
1. init => sort orders, sort trucks
2. for each order
    place_in_truck(order_size) -> return updates and sorts trucks
    
3. return trucks

Worst Case: n * mln(m)

"""

class ShippingOrder:
    def __init__(self, delivery_batch_id, number_of_pallets, customer_code):
        self._delivery_batch_id = delivery_batch_id
        self._number_of_pallets = number_of_pallets
        self.customer_code = customer_code

    def add_pallet(self):
        self._number_of_pallets += 1

    def get_size(self):
        return self._number_of_pallets

    def get_customer_code(self):
        return self.customer_code

    def __repr__(self):
        return f"{self.customer_code}[{self.get_size()}]"


class SemiTruck:
    def __init__(self, name, pallet_length=13):
        self.name = name
        self.length = pallet_length  # number of rows this truck can fit

    def get_total_capacity(self):
        return self.length * 4  # all trucks can fit 4 pallets per row

    # MinHeap
    def place_on_trucks(curr_order, trucks):
        while trucks:
            if curr_order <= trucks[0]: trucks[0] = trucks[0] - curr_order
            else:
               heapq.heappop(trucks)
            
ORDERS = [
    ShippingOrder(10,  3, 'FARMER_1039'),
    ShippingOrder(10,  7, 'FARMER_8265'),
    ShippingOrder(10,  1, 'FARMER_1100'),
    ShippingOrder(10,  2, 'FARMER_5858'),
    ShippingOrder(10,  4, 'FARMER_1727'),
    ShippingOrder(10,  3, 'FARMER_1123'),
    ShippingOrder(10,  9, 'FARMER_5662'),
    ShippingOrder(10, 12, 'FARMER_0708'),
    ShippingOrder(10,  8, 'FARMER_8863'),
    ShippingOrder(10,  7, 'FARMER_1025'),
    ShippingOrder(10, 14, 'FARMER_3755'),
    ShippingOrder(10, 11, 'FARMER_2520'),
    ShippingOrder(10, 12, 'FARMER_9729'),
    ShippingOrder(10,  8, 'FARMER_0185'),
    ShippingOrder(10,  6, 'FARMER_1884'),
    ShippingOrder(10, 19, 'FARMER_9122'),
    ShippingOrder(10, 18, 'FARMER_0103'),
    ShippingOrder(10, 16, 'FARMER_8681'),
    ShippingOrder(10, 12, 'FARMER_7229'),
    ShippingOrder(10,  7, 'FARMER_0395'),
    ShippingOrder(10, 15, 'FARMER_9967'),
    ShippingOrder(10, 11, 'FARMER_4301'),
    ShippingOrder(10,  5, 'FARMER_2125'),
    ShippingOrder(10,  6, 'FARMER_0587'),
]
# total pallets = 216

TRUCKS = [
    SemiTruck('Dakota Sunrise', pallet_length=13),
    SemiTruck('Mack Uphill', pallet_length=7),
    SemiTruck('Montana Cruiser', pallet_length=11),
    SemiTruck('Peter Rock', pallet_length=14),
    SemiTruck('Cloud Liner', pallet_length=9),
    # SemiTruck('Spare Minivan', pallet_length=2),
]
# total capacity: 216  (4 across each row), if you don't use the minivan "spare" truck.