Proyecto: Proyecto Final del curso de Python - Comisión 50215
Autor: Franco Lema
Versión: 1.0

Panel de Administración:

Usuario administrador: fr@n
Mail: franco_user@gmail.com
Password: abcd1234!

Considerar: python -m pip install Pillow

Cuando intento ejecutarlo desde otro equipo, me recomienda instalar este paquete

Objetivo: 

El objetivo del mismo es llevar adelante la administración interna de un local de fotocopias y soluciones gráficas. Es decir que solo los empleados y autorizados podrán acceder a la página, pero no los clientes

Descripción de modelos:

Modelo Libreria: Este modelo es en el que se guardan los datos de los productos que hay en stock, 
                subdividido en categoría de diferentes productos, ya que estos tienen distintas características
                Encontraremos Productos de artículos tales como: lapiceras, lápices, gomas, reglas, resaltadores, sacapuntas, cuadernos, libretas, liquid paper, etc.
                En esta subdivisión encontraremos un botón de búsqueda ya que se trata del modelo que más información tiene, y por lo tanto más difícil de investigar

Modelo Papel: Este modelo es en el que se guardan los datos de los productos relacionados al papel que se 
            utiliza en las fotocopias. Contienen la información del nombre del papel y la marca, 
            especificación de  su uso(fotográfico o común), tamaño, gramaje(peso en gramos) y su stock que se especifica en resmas(cajas de 500 hojas) o rollos en metros, ya que esto varía según su tipo.

Modelo Apunte: Este modelos se encarga de organizar el stock de apuntes que se venden en el local(Con el permiso del profesor a cargo de la cátedra) de distintas materias que se dictan en el CBC, separado por
                el nombre de la materia, cátedra y cantidad de ejemplares que están disponibles en ese momento para la venta

Modelo Tinta: Este modelo se encarga de organizar las diferentes tintas y sus usos, diferenciando el nombre junto con la marca, color, y si es para sublimación, ya que esta es un tipo de tinta especial para la impresión en telas

Modelo Empleado: Este modelo es para llevar el registro de los empleados que están trabajando en el local, donde una vez que estos se registran, deberá completar el template con sus datos, especificando su rol dentro del negocio

Modelo Cliente: Este modelo se encarga de llevar el registro de lo clientes habituales, es decir los que ya tienen cierta regularidad, tratandose de personas o empresas a los que el negocio se encarga de hacele impresiones.
                Por ejemplo, hacemos impresiones de los carteles de oferta a negocios que trabajan dentro del Alto Avellaneda Shopping

Modelo Contacto: Este modelo se encarga de llevar el registro de Proveedores habituales del negocio, es decir, a quienes se les compra los elementos con los que luego se harán las ventas, diferenciando quienes venden artículos de 
                librería o tintas, papel, toner(tinta para fotocopiadoras), especificando su email y número de teléfono para poder hacer consultas de presupuesto o cualquier otro tipo de contacto


Modelo Avatar: Este modelo es el que permite la creación y actualización del Avatar de usuario


Podrán notar que cada uno de estos elementos tiene una columna de acciones donde se podrá editar la información del artículo y eliminar el registro. También notarán una acción con el símbolo '+', la cual permite el agregado de registros y elementos. Solo los productos de 'Librería' tendrán un botón de acción de búsqueda que se identifica con el dibujo de una lupa, ya que se trata de la sección que más registros llevará, por lo tanto es el más difícil de administrar. El acceso a todas estas vistas y acciones solo lo tendrán aquellos que estén registrados y tengan un usuario que les permita acceder a la información de la página. Debajo encontrarán links de acceso a la página 'Acerca de mi' que tendrá la explicación de mi persona, un link que lleva a otra página con la ubicación del local, otro link que lleva a mi repositorio de GitHub y otro link que lleva a mi perfil de Linkedin. El link de 'Home' lleva a la cima de la página.

En la página 'Acerca de mi...' encontrarán debajo el link a 'Home' que permitirá volver de la vista de la página a la que se encuentran
