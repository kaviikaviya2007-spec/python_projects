print("\t\t\tIRIS FLOWER CLASSIFICATION")

sepal_length = float(input("Enter Sepal Length (cm): "))
sepal_width = float(input("Enter Sepal Width (cm): "))
petal_length = float(input("Enter Petal Length (cm): "))
petal_width = float(input("Enter Petal Width (cm): "))
flower_colour = input("Enter Flower Colour(Purple/Blue/White/Yellow/Pink): ")
leaf_colour = input("Enter Leaf Colour: ")

if petal_length < 2 and petal_width < 1:
    print("\nFlower Name : Iris Setosa")
elif petal_length < 5 and petal_width < 2:
    print("\nFlower Name : Iris Versicolor")
else:
    print("\nFlower Name : Iris Virginica")