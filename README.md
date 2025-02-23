# Shape Package
Este paquete proporciona una implementación de formas geométricas en Python, incluyendo puntos, líneas, rectángulos, cuadrados, triángulos y más. Se han realizado mejoras significativas para hacer el código más robusto, flexible y fácil de usar.

## Características principales
### Uso de @property:

Todas las propiedades protegidas de las clases se acceden mediante el decorador ``@property``. Esto permite un acceso controlado a los atributos internos de las clases.

````python
@property
def x(self):
    return self._x

@property
def y(self):
    return self._y

@property
def start_point(self):
    return self._start_point

@property
def end_point(self):
    return self._end_point

@property
def length(self):
    return self._length...
````

### Uso de @classmethod:

Se ha añadido un método de clase ``change_shape_type`` en la clase ``Shape`` para cambiar dinámicamente el tipo de forma (por ejemplo, convertir un conjunto de vértices en un rectángulo, cuadrado, triángulo, etc.).

````python
@classmethod
    def change_shape_type(cls, shape_type: str, vertices: list):
        """
        Método de clase para cambiar el tipo de forma.
        """
        match shape_type:
            case "Rectangle":
                return Rectangle(vertices[0], (vertices[1].x - vertices[0].x), (vertices[3].y - vertices[0].y))
            case "Square":
                return Square(vertices[0], (vertices[1].x - vertices[0].x))
            case "Triangle":
                return Triangle(vertices[0], vertices[1], vertices[2])...          
````
### Decorador personalizado timing_decorator:

Se ha implementado un decorador personalizado para medir el tiempo de ejecución de operaciones como ``compute_area`` y ``compute_perimeter``. Esto es útil para evaluar el rendimiento del código.

````python
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Tiempo inicial
        result = func(*args, **kwargs)  # Ejecutar la función decorada
        end_time = time.time()  # Tiempo final
        print(f"Tiempo de ejecución de {func.__name__}: {end_time - start_time:.6f} segundos")  # Mostrar el tiempo
        return result  # Retornar el resultado
    return wrapper  # Retornar la función wrapper
````

### Polimorfismo y herencia:

Las clases ``Rectangle``, ``Square``, ``Triangle``, ``Equilateral``, ``Isosceles``, ``Scalene`` y ``TriRectangle`` heredan de la clase base ``Shape``, lo que permite un diseño modular y extensible.

### Cálculos geométricos:

El paquete incluye métodos para calcular áreas, perímetros, distancias entre puntos, ángulos internos y más.

## Mejoras realizadas
### Acceso a propiedades protegidas:

Se han añadido decoradores ``@property`` para acceder a atributos como ``vertices``, ``edges``, ``inner_angles``, ``edge_lengths``, etc.

### Cambio dinámico de tipo de forma:

El método ``change_shape_type`` permite convertir un conjunto de vértices en diferentes tipos de formas (rectángulo, cuadrado, triángulo, etc.).

### Medición del tiempo de ejecución:

El decorador ``@timing_decorator`` mide y muestra el tiempo de ejecución de métodos como ``compute_area`` y ``compute_perimeter``.

### Código modular y reusable:

Las clases están diseñadas para ser extensibles, lo que permite añadir nuevas formas geométricas fácilmente.

## Estructura del código
### Clases principales
**1. Point:**

Representa un punto en un plano 2D con coordenadas (x, y).

- Métodos: ``compute_distance``, ``set_x``, ``set_y``.

- Propiedades: ``x``, ``y``.

**2. Line:**

Representa una línea entre dos puntos (``start_point`` y ``end_point``).

- Métodos: ``set_start_point``, ``set_end_point``.

- Propiedades: ``start_point``, ``end_point``, ``length``.

**3. Shape:**

Clase base para todas las formas geométricas.

- Métodos: ``edges``, ``regular``, ``compute_area``, ``compute_perimeter``, ``compute_inner_angles``, ``change_shape_type``.

- Propiedades: ``vertices``, ``inner_angles``, ``edge_``length``s``, ``value_edges``, ``is_regular``.

**4. Subclases de Shape:**

``Rectangle``, ``Square``, ``Triangle``, ``Equilateral``, ``Isosceles``, ``Scalene``, ``TriRectangle``.

Cada subclase implementa métodos específicos para calcular áreas y perímetros.

## Ejemplos de Uso:
Crear un rectángulo y calcular su área y perímetro
````python
print("\nTRIÁNGULO")
    tri = Triangle(Point(0, 0), Point(3, 0), Point(0, 4))

    print("Área del triangulo:", tri.compute_area())
    print("Perimetro del triangulo:", tri.compute_perimeter())
    print("Vértices:", tri.vertices)
    print("Bordes:", tri.value_edges)
    print("Longitudes de los lados:", tri.edge_lengths)
    print("Ángulos internos:", tri.inner_angles)
````

## Cambiar el tipo de forma:
````python
rectangle = Shape.change_shape_type("Rectangle", vertices)
    print("\nFigura a rectángulo:") 
    print("Área del rectángulo:", rectangle.compute_area())
    print("Perímetro del rectángulo:", rectangle.compute_perimeter())
````
