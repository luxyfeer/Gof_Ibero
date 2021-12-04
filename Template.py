"""Solución usando el patrón de diseño template"""

def obtener_texto(): 
      
    return "texto_plano"
  
def obtener_xml(): 
      
    return "xml"
  
def obtener_xls(): 
      
    return "xls"
  
def obtener_csv(): 
      
    return "csv"
  
def convertir_a_texto(datos): 
      
    print("[CONVERTIR]") 
    return "{} como texto".format(datos) 
  
def saver(): 
      
    print("[GUARDAR]") 
  
def template_fx(obteniendo, convirtiendo = False, para_guardar = False): 
  
    
    datos = obteniendo() 
    print("Obtener `{}`".format(datos)) 
  
    if len(datos) <= 3 and convirtiendo: 
        data = convirtiendo(datos) 
    else: 
        print("Saltar") 
      
    
    if para_guardar: 
        saver() 
  
    print("`{}` fue procesado".format(datos)) 
  
  
if __name__ == "__main__": 
  
    template_fx(obtener_xls, para_guardar = True) 
  
    template_fx(obtener_texto, para_guardar = convertir_a_texto) 
  
    template_fx(obtener_csv, para_guardar = True) 
  
    template_fx(obtener_xml, para_guardar = True) 