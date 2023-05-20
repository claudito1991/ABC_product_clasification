instructions_string = """
1) En las hojas A,B,C tenemos los productos con stock clasificados según la venta promedio diaria con el siguiente criterio:
Productos A: 80% de la venta promedio diaria
Productos B: 15% de la venta promedio diaria
Productos C: 5% de la venta promedio diaria

VPD: Venta promedio diaria 
STOCK: Stock del producto 
DIAS DE PISO: STOCK / VPD
CATEGORIA: Clasificación según VPD


2) En "Stats" se encuentra la información resumida de las tres categorías mencionadas.
Categoría: Clasificación ABC según se calculó previamente	
Valorizado: Dinero total por categoría de productos en stock
Peso porcentual (%): Cuanto pesa porcentualmente la categoría sobre el total. 
Target peso porcentual(%): Objetivo de peso de cada categoría según su representación en ventas.

3) Sin stock muestra aquellos productos con stock 0 pero que han tenido VPD mayor a 0 en los días evaluados
al sacar el reporte de punto de pedido. 


**Nota: aquellos SKU con stock menor a 1 se redondean a 0 para facilitar su clasificación posterior. 
"""

def read_py_instructions():
    lines = instructions_string.split("\n")
    return lines  

