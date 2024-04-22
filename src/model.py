epochs = 50
model1 = Sequential()
# Add convolution 2D
model1.add(Conv1D(filters=32,kernel_size=2,activation='relu',input_shape=(30,1)))
model1.add(BatchNormalization())
model1.add(Dropout(0.2))

model1.add(Conv1D(filters=64,kernel_size=2,activation='relu'))
model1.add(BatchNormalization())
model1.add(Dropout(0.5))

model1.add(Flatten())
model1.add(Dense(64,activation='relu'))
model1.add(Dropout(0.5))

model1.add(Dense(1,activation='sigmoid'))

# Compile the model without any optimization technique
model1.compile(loss=categorical_crossentropy,
              metrics=['accuracy'])
model1.save('saved_models/model1.pkl')

model1.summary()

# Train the model
history = model1.fit(X_train,y_train,epochs=epochs,validation_data=(X_test,y_test),verbose=1)

# Print the final accuracy
_, train_accuracy = model1.evaluate(X_train, y_train)
test_loss, test_accuracy = model1.evaluate(X_test, y_test)
print(f'Training Accuracy: {train_accuracy * 100:.2f}%')
print(f'Test Accuracy: {test_accuracy * 100:.2f}%')


import pickle 

filename = "model1.h5"
pickle.dump(model1, open(filename, 'wb'))


# loading the saved model

loaded_model1 = pickle.load(open('model1.h5', 'rb'))