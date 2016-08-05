from xml.dom import minidom

doc = minidom.parse("MulatOrg0913Envio091480.fmlr_disquete.xml")


rows = doc.getElementsByTagName("ROW")
for row in rows:
        sid = row.getAttribute("num")
        var_transaccion_afip = row.getElementsByTagName("TRANSACCION_AFIP")[0]
        var_registro = row.getElementsByTagName("REGISTRO")[0]
        var_c02n = row.getElementsByTagName("C02N")[0]
        print("Num:%s Transaccion AFIP:%s, Registro:%s, C02N:%s" % (sid, var_transaccion_afip.firstChild.data, var_registro.firstChild.data, var_c02n.firstChild.data))