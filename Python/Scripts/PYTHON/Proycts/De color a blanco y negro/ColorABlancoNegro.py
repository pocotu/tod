# convertir imagen a blanco y negro
from PIL import Image

#pip install Pillow

imagen = Image.open("D:\Algo\Win\AllProy\Python\Scripts\PYTHON\Proycts\De color a blanco y negro\michi.jpg")
BrancoYNegro = imagen.convert("L")
BrancoYNegro.save('D:\Algo\Win\AllProy\Python\Scripts\PYTHON\Proycts\De color a blanco y negro\BN_michi.')
BrancoYNegro.show()