import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [10, 25, 18, 30]
}

df = pd.DataFrame(data)

print(df)

plt.bar(df["Month"], df["Sales"])
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Sales by Month")
plt.show()

plt.hist(df["Sales"], bins=5)
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Distribution of Sales")
plt.show()
