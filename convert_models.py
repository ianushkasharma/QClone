import pickle
from joblib import dump

# Load old pickle models
rf = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('cv.pkl', 'rb'))

# Save as joblib
dump(rf, 'model.joblib')
dump(cv, 'cv.joblib')

print("Converted model.pkl and cv.pkl to joblib format!")
