model = keras.Sequential([
	keras.layers.Flatten(input_shape=(28, 28)), # input layer (1)
	keras.layers.Dense(128, activation='relu'), #hidden layer (2)
	keras.layers.Dense(10, activation='softmax') #output layer (3)
])

model.compile(optimizer='adam',
				loss='sparse_categorical_crossentropy.',
				metrics=['accuracy'])
model.fit(train_images, train_labes, ephochs=10)

test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=1)
print('Test accuracy:', test_acc)

predictions = model.predict(test_images)
print)class_names[np.argmx(prediction[2])]

### Convolutional Neural Networks###
