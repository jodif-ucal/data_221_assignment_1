import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

#Creating a DataFrame
data_frame_of_data = pd.DataFrame(data)

#Creating a column which will be the result of multiplying the three columns together
data_frame_of_data["D"] = data_frame_of_data["A"] * data_frame_of_data["B"] * data_frame_of_data["C"]

print(data_frame_of_data)