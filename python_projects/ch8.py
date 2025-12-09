
import numpy as np
array = np.arange(1, 11)
print("Mean:", np.mean(array))
print("Median:", np.median(array))
print("Standard Deviation:", np.std(array))
import pandas as pd
data={
    "Name": ["Mohamed", "ziad", "hadi", "Omar"],
    "Age": [20, 22, 21, 23],
    "Score": [85, 70, 95, 60]
}
df=pd.DataFrame(data)
result=df[df["Score"] > 80]
print(result)

import matplotlib.pyplot as plt
x = [1,2,3,4,5]
y = [1,4,9,16,25]
plt.plot(x, y)
plt.xlabel("x axis")
plt.ylabel("y axis")
plt.title("square numbers")
plt.show()

from flask import Flask
app = Flask(__name__)
@app.route('/hello')
def hello():
    return "Hello, Advanced Python!"
if __name__ == "__main__":
    app.run()

import torch
tensor1 = torch.tensor([1,2,3])
tensor2 = torch.tensor([4,5,6])
dot = torch.dot(tensor1, tensor2)
mul = tensor1 * tensor2
print("Dot Product:", dot)
print("Element-wise Multiplication:", mul)