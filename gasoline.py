import time
import os



class GasStation:
    print("Gas: 210 AMD || Petrol: 510 AMD || Diesel: 580 AMD")

    client = 0
    cistern_petrol = 1000
    cistern_diesel = 1000
    cistern_gas = 1000
    add_price_in_coupon = 0
    # add_liter_in_coupon = 0

    def __init__(self, type_, liter):
        self.type_ = type_
        self.liter = liter
        self.petrol = 0 #510
        self.gas = 0 #210
        self.diesel = 0 # 580
        self.time_now = time.strftime("%d/%m/ %H:%M:%S")

        if self.type_ == "petrol":
            GasStation.cistern_petrol -= self.liter
            print(self.petrol_())
        elif self.type_ == "diesel":
            GasStation.cistern_diesel -= self.liter
            print(self.diesel_())
        elif self.type_ == "gas":
            GasStation.cistern_gas -= self.liter
            print(self.gas_())

        print(self.store_coupon())
        GasStation.client += 1

    def petrol_(self):
        if self.cistern_petrol >= self.liter:
            for k in range(1, self.liter+1):
                self.petrol += 510
                print("\r", k, "Liter: ", "Money: ", self.petrol, end="")
                time.sleep(1)
            print()
            self.cistern_petrol -= self.liter
            return f"Date: {self.time_now} | {self.petrol}AMD "
        return "Not enough petrol"

    def diesel_(self):
        if self.cistern_diesel >= self.liter:
            for k in range(1, self.liter + 1):
                self.diesel += 580
                print("\r", k, "Liter: ", "Price: ", self.diesel, end="")
                time.sleep(1)
            print()
            self.cistern_diesel -= self.liter
            return f"Date: {self.time_now} | Price: {self.diesel}AMD "
        return "Not enough diesel"

    def gas_(self):
        if self.cistern_gas >= self.liter:
            for k in range(1, self.liter + 1):
                self.gas += 210
                print("\r", k, "Liter: ", "Price: ", self.gas, end="")
                time.sleep(1)
            print()
            self.cistern_gas -= self.liter
            return f"Date: {self.time_now} | Price: {self.gas}AMD "
        return "Not enough gas"

    def store_coupon(self):
        lst = ["-"*20, time.strftime("%d/%m/ %H:%M:%S")]
        if self.type_ == "petrol":
            self.add_price_in_coupon = self.liter * 510
        elif self.type_ == "diesel":
            self.add_price_in_coupon = self.liter * 580
        else:
            self.add_price_in_coupon = self.liter * 210

        lst.append(f"Price: {self.add_price_in_coupon} AMD | Liter: {self.liter}")
      
        with open("check.txt", "a") as file:
            for element in lst:
                file.write(str(element) + "\n")

        return ""
