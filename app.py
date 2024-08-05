from flask import Flask, jsonify, request

app = Flask(__name__)
  
def convertir(tiempo, entrada, salida):
    if entrada == 'h':
        if salida == 'm':
            return tiempo * 60
        elif salida == 's':
            return tiempo * 3600
        else:
            return tiempo
    elif entrada == 'm':
        if salida == 'h':
            return tiempo / 60
        elif salida == 's':
            return tiempo * 60
        else:
            return tiempo
    elif entrada == 's':
        if salida == 'h':
            return tiempo / 3600
        elif salida == 'm':
            return tiempo / 60
        else:
            return tiempo
        
@app.route('/convertir-tiempo',methods=['POST'])#Creacion de apirest
def convertir_tiempo():
    data=request.get_json()
    try:
        input_tiempo=data.get('tiempo')
       
        if type(input_tiempo)==int and type(data['entrada'])==str and type(data['salida'])==str:
            if (data['entrada']=='h' or data['entrada']=='m' or data['entrada']=='s') and (data['salida']=='h' or data['salida']=='m' or data['salida']=='s'):
                result=convertir(input_tiempo,data['entrada'],data['salida'])
            
            return jsonify({"tiempo": result,"unidad de salida":data['salida']})

    except KeyError:
        return jsonify({"Tiempo": None,"Error":"Verifique que tiempo sea un entero, que entrada y salida sean cadena (h, m ó s)"})


if __name__ == '__main__':
    app.run(debug=False) #PASO 1
    
#ESTO ESTA EN PRODUCTIVO...