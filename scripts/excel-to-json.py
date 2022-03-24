from fileinput import filename
import os
import pandas as pd

# directorio_actual = os.getcwd()

def scanDirectory(nameDir):

    dicFiles = {}
    with os.scandir(nameDir) as ficheros:
        for fichero in ficheros:
            if fichero.is_file() and '.xlsx' in fichero.name:
               #print('es archivo: ' + fichero.name)
               
               dicFiles[fichero.name.lower()] = nameDir + '\\' + fichero.name
               
            
            else:
                #print('Se enviará el directorio a scanear nuevamente: ' +(nameDir + '/' + fichero.name))
                dicFilesElse = scanDirectory(nameDir + '\\' + fichero.name)
                dicFiles.update(dicFilesElse)
    return dicFiles

def toPandas(dicFiles):
    listDF = []
    for nameFile, pathFile in dicFiles.items():

        # string = ''.join( x for x in string if x not in characters)
        df = pd.read_excel(pathFile,sheet_name=None)
        for key in df.keys():
            print(nameFile + '__' + key.lower())
            inputs =''.join( x for x in nameFile if x not in '.xlsx') + '__' + key.lower()
            print(inputs)
            exec(inputs + '= df[key]')
            df_shape = 'df_shape = df[key].shape'
            exec(df_shape)
            #print('dataframe creado: ' + inputs + '  =+=+=+=+  filas: ' + str(df_shape[0]) + '  =+=+=+=+  columnas: ' + str(df_shape[1]))
    return listDF


dicFiles = scanDirectory('C:\\Users\\alejo\\OneDrive\\Documentos\\git-repositories\\cne-cuentas-claras\\test-raw-info')
listDF = toPandas(dicFiles)
