# Insect-Classifier

This an classifier used to classify 12 types of household insects, implement based on TensorFlow and Keras
For the UI, implemented by PyQt5

  1. Ant
  2. Bee
  3. Butterfly
  4. Cockroaches
  5. Dragonfly
  6. Fly
  7. Grasshopper
  8. Ladybird
  9. Mosquito
  10. Scorpions
  11. Spiders
  12. Wasp
  
----
This repo propose 2 model
  1. InsectNet: Simplfied VGG16, same performance to VGG16 (Fewer parameters)
  2. Xception: Used transfer learning to train (Better performance)

Accuracy:
  1. InsectNet: Around 70%
  2. Xception: Around 80%

----

With techniques to reduce overfitting
  1. Dropout
  2. Early-Stopping

The overall accuracy is enhanced:
  1. InsectNet: 75%, stopped at 63 epochs out of 300
  2. Xception:  87%, stopped at 71 epochs out of 300

---

Install the required package

```
pip install -r requirements.txt
```

