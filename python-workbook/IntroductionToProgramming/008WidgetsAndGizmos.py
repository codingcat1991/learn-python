# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

WIDGETS_WEIGHT = 75
GIZMO_WEIGHT = 112

widgets = int(input('Enter the number of widgets: '))
gizmos = int(input('Enter the number of gizmos: '))

weight = widgets * WIDGETS_WEIGHT + gizmos + GIZMO_WEIGHT

print('the total weight of the order is', weight, 'grams')
