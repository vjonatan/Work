#!/usr/bin/env python
#
#


import os
import sys
import errno
import logging
from subprocess import Popen, call, PIPE
import re
import zipfile
import cx_Oracle

#Constantes para la conexion a la DB
#Testing
#DB_SERVER = 'aixtestin.mendoza.gov.ar' #Replica
#DB_PORT = 1521 #Replica
#DB_INSTANCE = 'TAXP'
#DB_USER = 'OSIRIS1'
#DB_PWD = 'osiris1'

#Produccion OSIRIS1
DB_SERVER = 'aixrentas.mendoza.gov.ar' #Produccion
DB_PORT = 1524 #Produccion
DB_INSTANCE = 'TAXP'
DB_USER = 'CONDMD29'
DB_PWD = 'CONDMD29'

#Constantes para la replicacion
#URL_COMARB = 'sftp://www.comarb.gov.ar'
#PORT_COMARB = '6969'
#DIR_ORIGEN_REPLIC = '/todas/sircreb/descargas/estadisticas/jur913'
#DIR_DESTINO_REPLIC = '/scripts/rentas/sircreb'
#USR_REPLIC = 'mcallaey'
#PWD_REPLIC = 'mcallaey'


DIR_LOG = '/scripts/rentas/log'

LFTP_CMD ='/usr/bin/lftp' 


#Constantes de errores (raise)
eLftpNoInstalado = 'ERROR: no esta instalado el comando lftp o no tiene permiso para ejecutarlo' 
#eReadOnlyDir = 'Error: el usuario no tiene permiso para escribir en el directorio %s' % (DIR_OPERACIONES)
#eReadOnlyDirErrores = 'Error: el usuario no tiene permiso para escribir en el directorio %s' % (DIR_ERRORES)

#Variable para la ruta al directorio
path = 'D:/Jona/Envio_XML-Envio_Cierre_Banco_XML/Archivos/'



def dbConnect():
    dsn = cx_Oracle.makedsn(DB_SERVER, DB_PORT, DB_INSTANCE)
    hdb = cx_Oracle.connect(DB_USER, DB_PWD, dsn)
    return hdb



def procesarNuevoArchivo(fileName):
    print 'Procesando archivo {0}....'.format(fileName)
    fileXml = open(fileName, "r")
    #print 'El directorio actual es {0}'.format(os.getcwd())
    #fileXml = open("MulatOrg0913Envio091480.fmlr_disquete.xml", "r")
    hdb = dbConnect()
	
    try:

        streamTxt = fileXml.read()

        try:

			cur = hdb.cursor()
			print "Ejecutando prc CONDMD29.procesar_xml..."
            
            # define variable object holding the nclob unicode data
			clobTxt = cur.var(cx_Oracle.CLOB)
            
			clobTxt.setvalue(0, streamTxt)
            
			rc = cur.var(cx_Oracle.STRING)

            
			fileNameMod = fileName
			cur.callproc('CONDMD29.procesar_xml', [clobTxt, rc])

			print 'Output de procesar_xml: {0}'.format(rc)

			cur.close()
			hdb.commit()
        finally:
			hdb.close()

    finally:
        print ''

    logging.info('  Archivo procesado :-)')



#def esArchivoDiario(fileName):
#    return re.match(r'^913_sircreb_20[0-9]{6}\.zip$', os.path.basename(fileName))



def main(argv=None):
    #Inicializar el log
#    initLogging()

#    if (getpass.getuser() != USER):
#        logging.error('Error: el programa debe ser ejecutado como el usuario {0}'.format(USER))
#        logging.error('Programa abortado!!!')
#        sys.exit(1)

    #Salvar el directorio actual para restaurarlo al final
    currDir = os.getcwd()

    try:
        logging.info('================================================================================')
        logging.info('Inicio proceso')
        print 'Inicio proceso'

        #Traer los nuevos archivos
        #(newFiles, updatedFiles) = syncRemote(True)
        '''
        if (newFiles) or (updateFiles):
            #Procesar los archivos nuevos
            for newFile in newFiles:
                #Procesar solo los archivos diarios, ignorar los mensuales
                if esArchivoDiario(newFile):
                    procesarNuevoArchivo(newFile)
                else:
                    logging.debug('Archivo mensual {0} ignorado'.format(newFile))

            #Procesar los archivos actualizados
            #NOTA: Analizar que se hara en estos casos.
            #         - Posibilidad 1: enviar un mail de que hay actualizaciones y cancelar el proceso
            #for updatedFile in updateFiles:
            #    procesarArchivoActualizado
        '''
        
        newFile = 'MulatOrg0913Envio091480.fmlr_disquete.xml'
        procesarNuevoArchivo(newFile)
        
        #archivo = open(newFile, "r") 
        #contenido = archivo.read()
        #print contenido
        
        #ficheros = os.listdir(path)
        #for newFile in ficheros:
        #    procesarNuevoArchivo(path + newFile)
        #    print newFile
        #    print '------------------------------------------------------'
        #    print '------------------------------------------------------'

    except Exception, err:
        logging.exception('Proceso abortado')
        print 'Proceso abortado. Log {0}'.format(err)
        return 1
    finally:
        # Restaurar el directorio actual
        os.chdir(currDir)
        return 0


if __name__ == "__main__":
    sys.exit(main())
