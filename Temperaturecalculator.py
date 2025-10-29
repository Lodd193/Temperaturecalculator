t = input("Enter temperature (e.g. 30C or 86F): ").strip().upper()
v, u = float(t[:-1]), t[-1]
print(f"{v}°{u} is {(v*9/5+32):.2f}°F" if u=="C" else f"{v}°{u} is {((v-32)*5/9):.2f}°C" if u=="F" else "Invalid input")
