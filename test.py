import pickle
import numpy as np

# Load the model from the pickle file
with open('iris_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Load or create your test data
# Here, we're using the same X_test from the previous step
# In practice, you will have your own test data
X_test = [[0.1,1.2,2.1,1.4]]

# Make predictions
prediction = model.predict(X_test)

# Print predictions
print(f'pred on test data {X_test}:',prediction)
