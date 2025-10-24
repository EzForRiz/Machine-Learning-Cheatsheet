# Code for predict() showing a single forward pass
def predict_label(x1, x2, w1, w2, w0):
  # Calcualte the value correcponding to the x and y values and the weights.
  val = x1*w1 + x2*w2 + 1*w0
  if val > 0:
    return 1
  else:
    return 0
  
acting=2.2 
direction=1.3     
label = predict_label(acting, direction, 1.1, 0.8, -5)

print('The moveie blongs to class:', label)