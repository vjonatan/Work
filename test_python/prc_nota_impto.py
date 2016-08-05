from xml.dom.minidom import parse
import xml.dom.minidom

# Open XML document using minidom parser
DOMTree = xml.dom.minidom.parse("MulatOrg0913Envio091480.nota_impto.xml")
collection = DOMTree.documentElement

# Get all the movies in the collection
movies = collection.getElementsByTagName("ROW")

if (movies.length > 0):
      
   for movie in movies:
      print "----------------------------------------------------------"
      print "*-*-*-*-*-*-*-*-*-*-*-*-*- ROW -*-*-*-*-*-*-*-*-*-*-*-*-*"
      print "----------------------------------------------------------"
      
      CIERRE_BANCO = movie.getElementsByTagName("CIERRE_BANCO")
      if (CIERRE_BANCO.length > 0):
         print "CIERRE_BANCO: %s" % CIERRE_BANCO[0].firstChild.data
      else:
         print "CIERRE_BANCO: ***"


      BANCO = movie.getElementsByTagName("BANCO")
      if (BANCO.length > 0):
         print "BANCO: %s" % BANCO[0].firstChild.data
      else:
         print "BANCO: ***"


      TIPO_NOTA = movie.getElementsByTagName("TIPO_NOTA")
      if (TIPO_NOTA.length > 0):
         print "TIPO_NOTA: %s" % TIPO_NOTA[0].firstChild.data
      else:
         print "TIPO_NOTA: ***"


      IMPUESTO = movie.getElementsByTagName("IMPUESTO")
      if (IMPUESTO.length > 0):
         print "IMPUESTO: %s" % IMPUESTO[0].firstChild.data
      else:
         print "IMPUESTO: ***"


      MONEDA = movie.getElementsByTagName("MONEDA")
      if (MONEDA.length > 0):
         print "MONEDA: %s" % MONEDA[0].firstChild.data
      else:
         print "MONEDA: ***"


      CUENTA = movie.getElementsByTagName("CUENTA")
      if (CUENTA.length > 0):
         print "CUENTA: %s" % CUENTA[0].firstChild.data
      else:
         print "CUENTA: ***"


      IMPORTE = movie.getElementsByTagName("IMPORTE")
      if (IMPORTE.length > 0):
         print "IMPORTE: %s" % IMPORTE[0].firstChild.data
      else:
         print "IMPORTE: ***"


      IMPORTE_IVA = movie.getElementsByTagName("IMPORTE_IVA")
      if (IMPORTE_IVA.length > 0):
         print "Importe_IVA: %s" % IMPORTE_IVA[0].firstChild.data
      else:
         print "Importe_IVA: ***"

      print ""

else:
   print "No hay registros en el archivo"