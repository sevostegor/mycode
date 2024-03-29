import numpy as np
import App
def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def derivative(x):
  func_x = sigmoid(x)
  return func_x * (1 - func_x)

def loss(y_true, y_pred):
  return ((y_true - y_pred) ** 2).mean()

class NeuNet:
 
  def __init__(self):
    self.w1 = np.random.normal()
    self.w2 = np.random.normal()
    self.w3 = np.random.normal()
    self.w4 = np.random.normal()
    self.w5 = np.random.normal()
    self.w6 = np.random.normal()
    self.w7 = np.random.normal()
    self.w8 = np.random.normal()
    self.w9 = np.random.normal()
    self.w10 = np.random.normal()
    self.w11 = np.random.normal()
    self.w12 = np.random.normal()
    self.w13 = np.random.normal()
    self.w14 = np.random.normal()
    self.w15 = np.random.normal()
    self.w16 = np.random.normal()
    self.w17 = np.random.normal()
    self.w18 = np.random.normal()
    self.w19 = np.random.normal()
    self.w20 = np.random.normal()
    self.w21 = np.random.normal()
    self.w22 = np.random.normal()
    self.w23 = np.random.normal()
    self.w24 = np.random.normal()
    self.w25 = np.random.normal()


    self.b1 = np.random.normal()
    self.b2 = np.random.normal()
    self.b3 = np.random.normal()
    self.b4 = np.random.normal()
    self.b5 = np.random.normal()
    self.b6 = np.random.normal()

  def feedforward(self, x):
    
    N1 = sigmoid(self.w1 * x[0] + self.w2 * x[1] + self.w11 * x[2] + self.w16 * x[3] + self.b1)
    N2 = sigmoid(self.w3 * x[0] + self.w4 * x[1] + self.w12 * x[2] + self.w17 * x[3] + self.b2)
    N3 = sigmoid(self.w5 * x[0] + self.w6 * x[1] + self.w13 * x[2] + self.w18 * x[3] + self.b3)
    N4 = sigmoid(self.w7 * x[0] + self.w8 * x[1] + self.w14 * x[2] + self.w19 * x[3] + self.b4)
    N5 = sigmoid(self.w9 * x[0] + self.w10 * x[1] + self.w15 * x[2] + self.w20 * x[3] + self.b5)
    sigma_1 = sigmoid(self.w21 * N1 + self.w22 * N2 + self.w23 * N3 + self.w24 * N4 + self.w25 * N5 + self.b6)
    return sigma_1

  def train(self, data, all_y_trues):
 
    learn_rate = 0.1
    epochs = 3000

    for epoch in range(epochs):
      for x, y_true in zip(data, y_trues):
        sum_N1 = self.w1 * x[0] + self.w2 * x[1] + self.w11 * x[2] + self.w16 * x[3] + self.b1
        N1 = sigmoid(sum_N1)

        sum_N2 = self.w3 * x[0] + self.w4 * x[1] + self.w12 * x[2] + self.w17 * x[3] + self.b2
        N2 = sigmoid(sum_N2)

        sum_N3 = self.w5 * x[0] + self.w6 * x[1] + self.w13 * x[2] + self.w18 * x[3] + self.b3
        N3 = sigmoid(sum_N3)

        sum_N4 = self.w7 * x[0] + self.w8 * x[1] + self.w14 * x[2] + self.w19 * x[3] + self.b4
        N4 = sigmoid(sum_N4)

        sum_N5 = self.w9 * x[0] + self.w10 * x[1] + self.w15 * x[2] + self.w20 * x[3] + self.b5
        N5 = sigmoid(sum_N5)

        sum_sigma_1 = self.w21 * N1 + self.w22 * N2 + self.w23 * N3 + self.w24 * N4 + self.w25 * N5 + self.b6
        sigma_1 = sigmoid(sum_sigma_1)
        y_pred = sigma_1

        
        p_L_p_ypred = -2 * (y_true - y_pred)

        
        p_ypred_p_w21 = N1 * derivative(sum_sigma_1)
        p_ypred_p_w22 = N2 * derivative(sum_sigma_1)
        p_ypred_p_w23 = N3 * derivative(sum_sigma_1)
        p_ypred_p_w24 = N4 * derivative(sum_sigma_1)
        p_ypred_p_w25 = N5 * derivative(sum_sigma_1)
        p_ypred_p_b6 = derivative(sum_sigma_1)

        p_ypred_p_N1 = self.w21 * derivative(sum_sigma_1)
        p_ypred_p_N2 = self.w22 * derivative(sum_sigma_1)
        p_ypred_p_N3 = self.w23 * derivative(sum_sigma_1)
        p_ypred_p_N4 = self.w24 * derivative(sum_sigma_1)
        p_ypred_p_N5 = self.w25 * derivative(sum_sigma_1)
        

        
        p_N1_p_w1 = x[0] * derivative(sum_N1)
        p_N1_p_w2 = x[1] * derivative(sum_N1)
        p_N1_p_w11 = x[2] * derivative(sum_N1)
        p_N1_p_w12 = x[3] * derivative(sum_N1)
        p_N1_p_b1 = derivative(sum_N1)

        
        p_N2_p_w3 = x[0] * derivative(sum_N2)
        p_N2_p_w4 = x[1] * derivative(sum_N2)
        p_N2_p_w13 = x[2] * derivative(sum_N2)
        p_N2_p_w14 = x[3] * derivative(sum_N2)
        p_N2_p_b2 = derivative(sum_N2)

        
        p_N3_p_w5 = x[0] * derivative(sum_N3)
        p_N3_p_w6 = x[1] * derivative(sum_N3)
        p_N3_p_w15 = x[2] * derivative(sum_N3)
        p_N3_p_w16 = x[3] * derivative(sum_N3)
        p_N3_p_b3 = derivative(sum_N3)

       
        p_N4_p_w7 = x[0] * derivative(sum_N4)
        p_N4_p_w8 = x[1] * derivative(sum_N4)
        p_N4_p_w17 = x[2] * derivative(sum_N4)
        p_N4_p_w18 = x[3] * derivative(sum_N4)
        p_N4_p_b4 = derivative(sum_N4)

        
        p_N5_p_w9 = x[0] * derivative(sum_N5)
        p_N5_p_w10 = x[1] * derivative(sum_N5)
        p_N5_p_w19 = x[2] * derivative(sum_N5)
        p_N5_p_w20 = x[3] * derivative(sum_N5)
        p_N5_p_b5 = derivative(sum_N5)

        
        self.w1 -= learn_rate * p_L_p_ypred * p_ypred_p_N1 * p_N1_p_w1
        self.w2 -= learn_rate * p_L_p_ypred * p_ypred_p_N1 * p_N1_p_w2
        self.w11 -= learn_rate * p_L_p_ypred * p_ypred_p_N1 * p_N1_p_w11
        self.w12 -= learn_rate * p_L_p_ypred * p_ypred_p_N1 * p_N1_p_w12
        self.b1 -= learn_rate * p_L_p_ypred * p_ypred_p_N1 * p_N1_p_b1

        
        self.w3 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N2_p_w3
        self.w4 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N2_p_w4
        self.w13 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N2_p_w13
        self.w14 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N2_p_w14
        self.b2 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N2_p_b2

        self.w5 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N3_p_w5
        self.w6 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N3_p_w6
        self.w15 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N3_p_w15
        self.w16 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N3_p_w16
        self.b3 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N3_p_b3

        self.w7 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N4_p_w7
        self.w8 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N4_p_w8
        self.w17 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N4_p_w17
        self.w18 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N4_p_w18
        self.b4 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N4_p_b4

        self.w9 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N5_p_w9
        self.w10 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N5_p_w10
        self.w19 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N5_p_w19
        self.w20 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N5_p_w20
        self.b5 -= learn_rate * p_L_p_ypred * p_ypred_p_N2 * p_N5_p_b5

       
        self.w21 -= learn_rate * p_L_p_ypred * p_ypred_p_w21
        self.w22 -= learn_rate * p_L_p_ypred * p_ypred_p_w22
        self.w23 -= learn_rate * p_L_p_ypred * p_ypred_p_w23
        self.w24 -= learn_rate * p_L_p_ypred * p_ypred_p_w24
        self.w25 -= learn_rate * p_L_p_ypred * p_ypred_p_w25
        self.b6 -= learn_rate * p_L_p_ypred * p_ypred_p_b6

      
      if epoch % 10 == 0:
        y_preds = np.apply_along_axis(self.feedforward, 1, data)
        losses = loss(all_y_trues, y_preds)
        print("Epoch %d losses: %.3f" % (epoch, losses))


data = np.array([
  [86, 12, 23, 4],  
  [31, 74, 13, 1],   
  [79, 25, 63, 0],   
  [43, 39, 32, 79],
  [21, 84, 0, 89],  
  [45, 40, 46, 47],
  [87, 3, 78, 84]
])
y_trues = np.array([
  0,
  1,
  0,
  1,
  1,
  1,
  1
])


network = NeuNet()
network.train(data, y_trues)


def prognoz():
  aa = []
  with open(r"file.txt", "r") as file:
    for line in file:
      aa.append(line)

  a = int(float(aa[0]))
  b = int(float(aa[1]))
  c = int(float(aa[2]))
  d = int(float(aa[3]))
  print(aa)
  
  year_1 = np.array([a, b, c, d])
  k = network.feedforward(year_1)
  return k
