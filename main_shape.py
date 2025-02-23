from reto_09.shape import *

def main():
    print("RECTÁNGULO") 
    rectangle = Rectangle(Point(0, 0), width=4, height=2)

    print("Área del rectángulo:", rectangle.compute_area())
    print("Perímetro del rectángulo:", rectangle.compute_perimeter())
    print("Vértices:", rectangle.vertices)
    print("Bordes:", rectangle.value_edges)
    print("Longitudes de los lados:", rectangle.edge_lengths)
    print("Ángulos internos:", rectangle.inner_angles)

    print("\nCUADRADO")
    square = Square(Point(0,0), side=5)

    print("Área del cuadrado:", square.compute_area())
    print("Perímetro del cuadrado:", square.compute_perimeter())
    print("Vértices:", square.vertices)
    print("Bordes:", square.value_edges)
    print("Longitudes de los lados:", square.edge_lengths)
    print("Ángulos internos:", square.inner_angles)

    print("\nTRIÁNGULO")
    tri = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))

    print("Área del triangulo:", tri.compute_area())
    print("Perimetro del triangulo:", tri.compute_perimeter())
    print("Vértices:", tri.vertices)
    print("Bordes:", tri.value_edges)
    print("Longitudes de los lados:", tri.edge_lengths)
    print("Ángulos internos:", tri.inner_angles)

    print("\nTRIÁNGULO EQUILÁTERO")
    eq = Equilateral(Point(0, 0), side=5)

    print("Área de un triangulo equilátero:", eq.compute_area())
    print("Perimetro de un triangulo equilátero:", eq.compute_perimeter())
    print("Vértices:", eq.vertices)
    print("Bordes:", eq.value_edges)    
    print("Longitudes de los lados:", eq.edge_lengths)
    print("Ángulos internos:", eq.inner_angles)

    print("\nTRIÁNGULO ISOSCELES")
    iso = Isosceles(Point(0, 0), base=4, side=5)

    print("Área del triangulo isosceles:", iso.compute_area())
    print("Perimetro de un triangulo equilátero:", iso.compute_perimeter())
    print("Vértices:", iso.vertices)
    print("Bordes:", iso.value_edges)
    print("Longitudes de los lados:", iso.edge_lengths)
    print("Ángulos internos:", iso.inner_angles)

    print("\nTRIÁNGULO ESCALENO")
    sca = Scalene(Point(0, 0), Point(4, 0), Point(2, 3))

    print("Área del triangulo isosceles:", sca.compute_area())
    print("Perimetro de un triangulo equilátero:", sca.compute_perimeter())
    print("Vértices:", sca.vertices)
    print("Bordes:", sca.value_edges)
    print("Longitudes de los lados:", sca.edge_lengths)
    print("Ángulos internos:", sca.inner_angles)

    print("\nTRIÁNGULO RECTÁNGULO")
    tri_rect = TriRectangle(Point(0, 0), base=3, height=4)

    print("Área del triangulo isosceles:", tri_rect.compute_area())
    print("Perimetro de un triangulo equilátero:", tri_rect.compute_perimeter())
    print("Vértices:", tri_rect.vertices)
    print("Bordes:", tri_rect.value_edges)
    print("Longitudes de los lados:", tri_rect.edge_lengths)
    print("Ángulos internos:", tri_rect.inner_angles)

    print("\nCAMBIAR FORMA:")
    
    # Crear una forma a partir de una lista de vértices
    vertices = [Point(0, 0), Point(4, 0), Point(4, 3), Point(0, 3)]
    shape = Shape(vertices)
    print(f"Vertives: {shape.vertices}")  # [Point(x=0, y=0), Point(x=4, y=0), Point(x=4, y=3), Point(x=0, y=3)]

    # Cambiar el tipo de forma a un rectángulo
    rectangle = Shape.change_shape_type("Rectangle", vertices)
    print("\nFigura a rectángulo:") 
    print("Área del rectángulo:", rectangle.compute_area())
    print("Perímetro del rectángulo:", rectangle.compute_perimeter())
    
    # Cambiar el tipo de forma a un triángulo
    print("\nFigura a triangulo:")
    triangle = Shape.change_shape_type("Triangle", vertices)
    print("Área del rectángulo:", triangle .compute_area())
    print("Perímetro del rectángulo:", triangle .compute_perimeter())
    
    # Cambiar el tipo de forma a un cuadrado
    print("\nFigura a cuadrado:")
    square = Shape.change_shape_type("Square", vertices)
    print("Área del cuadrado:", square.compute_area())
    print("Perímetro del cuadrado:", square.compute_perimeter())
    
    # Cambiar el tipo de forma a un triángulo equilátero
    print("\nFigura a triángulo equilátero:")
    equilateral = Shape.change_shape_type("Equilateral", vertices)
    print("Área del triángulo equilátero:", equilateral.compute_area())
    print("Perímetro del triángulo equilátero:", equilateral.compute_perimeter())
    
    # Cambiar el tipo de forma a un triángulo isósceles
    print("\nFigura a triángulo isósceles:")
    isosceles = Shape.change_shape_type("Isosceles", vertices)
    print("Área del triángulo isósceles:", isosceles.compute_area())
    print("Perímetro del triángulo isósceles:", isosceles.compute_perimeter())
    
    # Cambiar el tipo de forma a un triángulo escaleno
    print("\nFigura a triángulo escaleno:")
    scalene = Shape.change_shape_type("Scalene", vertices)
    print("Área del triángulo escaleno:", scalene.compute_area())
    print("Perímetro del triángulo escaleno:", scalene.compute_perimeter())
    
    # Cambiar el tipo de forma a un triángulo rectángulo
    print("\nFigura a triángulo rectángulo:")
    tri_rectangle = Shape.change_shape_type("TriRectangle", vertices)
    print("Área del triángulo rectángulo:", tri_rectangle.compute_area())
    print("Perímetro del triángulo rectángulo:", tri_rectangle.compute_perimeter())
    
if __name__ == "__main__":
    main()  