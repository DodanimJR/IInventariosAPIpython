from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api,reqparse
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/inventario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
api = Api(app)

## parser para el metodo POST de item
parser1=reqparse.RequestParser()
parser1.add_argument('nombre',help='Por favor indica el nombre , no puede estar en blanco',required=True)
parser1.add_argument('codigoId',help='Por favor indica el CodigoId',required=True)
parser1.add_argument('precio',help='Por favor indica el precio, no puede estar en blanco',required=True)
parser1.add_argument('categoria',help='Por favor indica la categoria, no puede estar en blanco')
parser1.add_argument('foto',help='Por favor indica la URL de la foto')
parser1.add_argument('descripcion',help='Por favor indica la descripcion, no puede estar en blanco')
parser1.add_argument('anotacionDeGerente',help='Por favor indica la anotacion del gerente')
## parser para el metodo PUT de item
parser2=reqparse.RequestParser()
parser2.add_argument('nombre',help='Por favor indica el nombre , no puede estar en blanco')
parser2.add_argument('codigoId',help='Por favor indica el CodigoId')
parser2.add_argument('precio',help='Por favor indica el precio, no puede estar en blanco')
parser2.add_argument('categoria',help='Por favor indica la categoria, no puede estar en blanco')
parser2.add_argument('foto',help='Por favor indica la URL de la foto')
parser2.add_argument('descripcion',help='Por favor indica la descripcion, no puede estar en blanco')
parser2.add_argument('anotacionDeGerente',help='Por favor indica la anotacion del gerente')

## parser para el metodo POST de empleado
parser3=reqparse.RequestParser()
parser3.add_argument('nombre',help='Por favor indica el nombre , no puede estar en blanco',required=True)
parser3.add_argument('codigoId',help='Por favor indica el CodigoId',required=True)
parser3.add_argument('puesto',help='Por favor indica el puesto, no puede estar en blanco',required=True)
parser3.add_argument('rol',help='Por favor indica el rol, no puede estar en blanco',required=True)
parser3.add_argument('foto',help='Por favor indica la URL de la foto')
parser3.add_argument('descripcion',help='Por favor indica la descripcion, no puede estar en blanco')
parser3.add_argument('anotacionDeGerente',help='Por favor indica la anotacion del gerente')
## parser para el metodo PUT de empleado
parser4=reqparse.RequestParser()
parser4.add_argument('nombre',help='Por favor indica el nombre')
parser4.add_argument('codigoId',help='Por favor indica el CodigoId')
parser4.add_argument('puesto',help='Por favor indica el puesto')
parser4.add_argument('rol',help='Por favor indica el rol')
parser4.add_argument('foto',help='Por favor indica la URL de la foto')
parser4.add_argument('descripcion',help='Por favor indica la descripcion')



##Modelo de la tabla Items
class Item(db.Model):
    nombre=db.Column(db.String(100),nullable=False)
    codigoId=db.Column(db.Integer,primary_key=True)
    precio=db.Column(db.Integer,nullable=False)
    categoria=db.Column(db.String(255),nullable=True)
    foto=db.Column(db.String(255),nullable=True)
    descripcion=db.Column(db.String(255),nullable=True)
    anotacionGerente=db.Column(db.String(255),nullable=True)

    def __repr__(self) -> str:
        return super().__repr__()

## Modelo de la tabla empleados    
class Empleado(db.Model):
    nombre=db.Column(db.String(100),nullable=False)
    codigoId=db.Column(db.Integer,primary_key=True)
    puesto=db.Column(db.String(200),nullable=False)
    rol=db.Column(db.String(255),nullable=True)
    foto=db.Column(db.String(255),nullable=True)
    descripcion=db.Column(db.String(255),nullable=True)
    anotacionGerente=db.Column(db.String(255),nullable=True)

    def __repr__(self) -> str:
        return super().__repr__()

db.create_all()
##Index default
class IndexRoute(Resource):
    def get(self):
        return {'response': 'ESTE ES EL INDES ROUTE SIYY'},200
##Ruta de los items
class IndexRouteItems(Resource):
    ## metodo GET ALL ITEMS
    def get(self):
        items=Item.query.all()
        response=[]
        if items:
            for item in items:
                response.append({
                    "nombre":item.nombre,
                    "codigoId":item.codigoId,
                    "precio":item.precio,
                    "categoria":item.categoria,
                    "foto":item.foto,
                    "descripcion":item.descripcion,
                    "anotacionDeGerente":item.anotacionGerente
                })
            return {'response':response},302
        else:
            return {'response':"No se encontraron registros"},404
    ## metodo POST Items
    def post(self):
        args1=parser1.parse_args()
        item=Item(nombre=args1['nombre'],codigoId=args1['codigoId'],precio=args1['precio'],categoria=args1['categoria'],foto=args1['foto'],descripcion=args1['descripcion'],anotacionGerente=args1['anotacionDeGerente'],)
        db.session.add(item)
        db.session.commit()
        return{'response':"Item agregado exitosamente"},201

class ItemsByID(Resource):
    ## metodo GET items by ID
    def get(self,id):
        item=Item.query.filter_by(codigoId=id).first()
        response=[]
        if item:     
            response.append({
                "nombre":item.nombre,
                "codigoId":item.codigoId,
                "precio":item.precio,
                "categoria":item.categoria,
                "foto":item.foto,
                "descripcion":item.descripcion,
                "anotacionDeGerente":item.anotacionGerente
            })
            return {'response':response},302
        else:
            return {'response':"No se encontraron registros de items, revise el id "+ str(id)},404
    def put(self,id):
        item=Item.query.filter_by(codigoId=id).first()
        if item:
            datos=parser2.parse_args()
            ##verificacion de datos del update
            if(datos['nombre']==None and datos['codigoId']==None and datos['precio']==None and datos['categoria']==None and datos['foto']==None and datos['descripcion']==None and datos['anotacionDeGerente']==None):
                return{"response":"Formato no valido :|"},400
            ## Realizar los cambios existentes
            elif datos['nombre']:
                item.nombre =datos['nombre']
            elif datos['codigoId']:
                item.codigoId =datos['codigoId']
            elif datos['precio']:
                item.precio =datos['precio']
            elif datos['categoria']:
                item.categoria =datos['categoria']
            elif datos['foto']:
                item.foto =datos['foto']
            elif datos['descripcion']:
                item.descripcion =datos['descripcion']
            db.session.commit()
            return{'response':"Item con id: "+str(id)+" actualizado correctamente"},202
        else:
            return {'response':"No se encontraron registros de items, revise el id "+ str(id)},404
             
    ## metodo DELETE de item
    def delete(self, id):
        item=Item.query.filter_by(codigoId=id).first()
        db.session.delete(item)
        db.session.commit()
        if item:
            return{'response':"Item con id: "+str(id)+" borrado correctamente"},302
        else:
            return {'response':"No se encontraron registros de items, revise el id "+ str(id)},404
##Ruta de Empleados        

class IndexRouteEmpleados(Resource):
        ## metodo GET ALL empleados
    def get(self):
        empleados=Empleado.query.all()
        response=[]
        if empleados:
            for empleado in empleados:
                response.append({
                    "nombre":empleado.nombre,
                    "codigoId":empleado.codigoId,
                    "puesto":empleado.puesto,
                    "rol":empleado.rol,
                    "foto":empleado.foto,
                    "descripcion":empleado.descripcion,
                    "anotacionDeGerente":empleado.anotacionGerente
                })
            return {'response':response},302
        else:
            return {'response':"No se encontraron registros"},404
    ## metodo POST Empleados
    def post(self):
        args1=parser3.parse_args()
        empleado=Empleado(nombre=args1['nombre'],codigoId=args1['codigoId'],puesto=args1['puesto'],rol=args1['rol'],foto=args1['foto'],descripcion=args1['descripcion'],anotacionGerente=args1['anotacionDeGerente'])
        db.session.add(empleado)
        db.session.commit()
        return{'response':"Empleado agregado exitosamente"},201

class EmpleadosByID(Resource):
    ## metodo GET Empleados by ID
    def get(self,id):
        empleado=Empleado.query.filter_by(codigoId=id).first()
        response=[]
        if empleado:     
            response.append({
                    "nombre":empleado.nombre,
                    "codigoId":empleado.codigoId,
                    "puesto":empleado.puesto,
                    "rol":empleado.rol,
                    "foto":empleado.foto,
                    "descripcion":empleado.descripcion,
                    "anotacionDeGerente":empleado.anotacionGerente
                })
            return {'response':response},302
        else:
            return {'response':"No se encontraron registros de empleados, revise el id "+ str(id)},404
    ## UPDATE empleados
    def put(self,id):
        empleado=Empleado.query.filter_by(codigoId=id).first()
        if empleado:
            print(empleado.nombre)
            datos=parser4.parse_args()
            print(datos)
            ##verificacion de datos del update
            if(datos['nombre']==None and datos['codigoId']==None and datos['puesto']==None and datos['rol']==None and datos['foto']==None and datos['descripcion']==None):
                return{"response":"Formato no valido :|"},400
            ## Realizar los cambios existentes
            if datos['nombre']:
                empleado.nombre =datos['nombre']
            elif datos['codigoId']:
                empleado.codigoId =datos['codigoId']
            elif datos['puesto']:
                empleado.puesto =datos['puesto']
            elif datos['rol']:
                empleado.rol =datos['rol']
            elif datos['foto']:
                empleado.foto =datos['foto']
            elif datos['descripcion']:
                empleado.descripcion =datos['descripcion']
            db.session.commit()
            return{'response':"Empleado con id: "+str(id)+" actualizado correctamente"},202
        else:
            return {'response':"No se encontraron registros de empleados, revise el id "+ str(id)},404
             
    ## metodo DELETE de Empleados
    def delete(self, id):
        empleado=Empleado.query.filter_by(codigoId=id).first()
        db.session.delete(empleado)
        db.session.commit()
        if empleado:
            return{'response':"Empleado con id: "+str(id)+" borrado correctamente"},302
        else:
            return {'response':"No se encontraron registros de empleados, revise el id "+ str(id)},404























api.add_resource(IndexRoute,'/')
api.add_resource(IndexRouteItems,'/items')
api.add_resource(ItemsByID,'/items/<int:id>')
api.add_resource(IndexRouteEmpleados,'/empleados')
api.add_resource(EmpleadosByID,'/empleados/<int:id>')
