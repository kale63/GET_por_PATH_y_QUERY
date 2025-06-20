from fastapi import FastAPI
from pydantic import BaseModel
import csv

app = FastAPI()

# Actividad 1: GET de la API

class Alumnos(BaseModel):
    Matricula: str
    Nombre: str
    Edad: int
    Genero: str
    Carrera: str
    Semestre: int
    Trabajo: str
    Estado: str
    Hobby: str
    Preferencia: str
    
# Importar la lista de alumnos

classmates_list = []

with open('COPIA_bdmodelos.csv', newline='', encoding='utf-8-sig') as file:
    reader = csv.DictReader(file, delimiter=',')
    print("CSV headers:", reader.fieldnames)
    
    for row in reader:
        classmate = Alumnos(
            Matricula=row["Matricula"],
            Nombre=row["Nombre"],
            Edad=int(row["Edad"]),
            Genero=row["Genero"],
            Carrera=row["Carrera"],
            Semestre=int(row["Semestre"]),
            Trabajo=row["Trabajo"],
            Estado=row["Estado"],
            Hobby=row["Hobby"],
            Preferencia=row["Preferencia"]
        )
        classmates_list.append(classmate)
        
# Endpoint por PATH

@app.get("/alumnos/{matricula}")
async def get_classmate(matricula: str):
    filtered_classmates = filter(lambda c: c.Matricula == matricula, classmates_list)
    result = list(filtered_classmates)
    return result[0] if result else {"error": "Alumno no encontrado"}

@app.get("/alumnos/edad/{edad}")
async def get_classmates_by_age(edad: int):
    filtered_classmates = filter(lambda c: c.Edad == edad, classmates_list)
    result = list(filtered_classmates)
    return result if result else {"error": "No se encontraron alumnos con esa edad"}

@app.get("/alumnos/nombre/{nombre}")
async def get_classmates_by_name(nombre: str):
    filtered_classmates = filter(lambda c: nombre.lower() in c.Nombre.lower(), classmates_list)
    result = list(filtered_classmates)
    return result if result else {"error": "No se encontraron alumnos con ese nombre"}

@app.get("/alumnos/genero/{genero}")
async def get_classmates_by_gender(genero: str):
    filtered_classmates = filter(lambda c: c.Genero.lower() == genero.lower(), classmates_list)
    result = list(filtered_classmates)
    return result if result else {"error": "No se encontraron alumnos con ese género"}

@app.get("/alumnos/semestre/{semestre}")
async def get_classmates_by_semester(semestre: int):
    filtered_classmates = filter(lambda c: c.Semestre == semestre, classmates_list)
    result = list(filtered_classmates)
    return result if result else {"error": "No se encontraron alumnos en ese semestre"}

@app.get("/alumnos/trabajo/{trabajo}")
async def get_classmates_by_job(trabajo: str):
    filtered_classmates = filter(lambda c: c.Trabajo.lower() == trabajo.lower(), classmates_list)
    result = list(filtered_classmates)
    return result if result else {"error": "No se encontraron alumnos que coincidan con esa situación laboral"}

@app.get("/alumnos/estado/{estado}")
async def get_classmates_by_state(estado: str):
    filtered_classmates = filter(lambda c: c.Estado.lower() == estado.lower(), classmates_list)
    result = list(filtered_classmates)
    return result if result else {"error": "No se encontraron alumnos que vengan de ese estado"}

@app.get("/alumnos/carrera/{carrera}")
async def get_classmates_by_career(carrera: str):
    filtered_classmates = filter(lambda c: c.Carrera.lower() == carrera.lower(), classmates_list)
    result = list(filtered_classmates)
    return result if result else {"error": "No se encontraron alumnos en esa carrera"}

@app.get("/alumnos/hobby/{hobby}")
async def get_classmates_by_hobby(hobby: str):
    filtered_classmates = filter(lambda c: hobby.lower() in c.Hobby.lower(), classmates_list)
    result = list(filtered_classmates)
    return result if result else {"error": "No se encontraron alumnos con ese hobby"}

@app.get("/alumnos/preferencia/{preferencia}")
async def get_classmates_by_preference(preferencia: str):
    filtered_classmates = filter(lambda c: preferencia.lower() in c.Preferencia.lower(), classmates_list)
    result = list(filtered_classmates)
    return result if result else {"error": "No se encontraron alumnos con esa preferencia"}

# Actividad 2: Endpoints por query

# Endpoint para obtener la lista completa de alumnos
@app.get("/alumnos/")
async def get_classmates():
    return classmates_list

@app.get("/por_matricula")
async def get_by_matricula(matricula: str):
    result = filter(lambda a: a.Matricula == matricula.lower, classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontró el alumno con esa matrícula"}

@app.get("/por_nombre")
async def get_by_nombre(nombre: str):
    result = filter(lambda a: nombre.lower() in a.Nombre.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos con ese nombre"}

@app.get("/por_genero")
async def get_by_genero(genero: str):
    result = filter(lambda a: a.Genero.lower() == genero.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos de ese género"}

@app.get("/por_estado")
async def get_by_estado(estado: str):
    result = filter(lambda a: a.Estado.lower() == estado.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos que vengan de ese estado"}

@app.get("/por_edad_y_genero")
async def get_by_edad_and_genero(edad: int, genero: str):
    result = filter(lambda a: a.Edad == edad and a.Genero.lower() == genero.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos con esa edad y género"}

@app.get("/por_semestre_y_trabajo")
async def get_by_semestre_and_trabajo(semestre: int, trabajo: str):
    result = filter(lambda a: a.Semestre == semestre and a.Trabajo.lower() == trabajo.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos con ese semestre y situación laboral"}

@app.get("/por_genero_y_hobby")
async def get_by_genero_and_hobby(genero: str, hobby: str):
    result = filter(lambda a: a.Genero.lower() == genero.lower() and hobby.lower() in a.Hobby.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos con ese género y ese hobby"}

@app.get("/por_edad_y_carrera")
async def get_by_edad_and_carrera(edad: int, carrera: str):
    result = filter(lambda a: a.Edad == edad and a.Carrera.lower() == carrera.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos con esa edad y de ese carrera"}

@app.get("/por_estado_y_carrera")
async def get_by_estado_and_carrera(estado: str, carrera: str):
    result = filter(lambda a: a.Estado.lower() == estado.lower() and a.Carrera.lower() == carrera.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos de ese estado y en esa carrera"}

@app.get("/por_carrera_y_hobby")
async def get_by_carrera_and_hobby(carrera: str, hobby: str):
    result = filter(lambda a: a.Carrera.lower() == carrera.lower() and hobby.lower() in a.Hobby.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos de esa carrera y con ese hobby"}

@app.get("/por_genero_y_preferencia")
async def get_by_genero_and_preferencia(genero: str, preferencia: str):
    result = filter(lambda a: a.Genero.lower() == genero.lower() and preferencia.lower() in a.Preferencia.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos de ese género y con esa preferencia"}

@app.get("/por_nombre_y_carrera")
async def get_by_nombre_and_carrera(nombre: str, carrera: str):
    result = filter(lambda a: nombre.lower() in a.Nombre.lower() and a.Carrera.lower() == carrera.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos con ese nombre y de esa carrera"}

@app.get("/por_nombre_y_edad")
async def get_by_nombre_and_edad(nombre: str, edad: int):
    result = filter(lambda a: nombre.lower() in a.Nombre.lower() and a.Edad == edad, classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos con ese nombre y edad"}

@app.get("/por_carrera_y_preferencia")
async def get_by_carrera_and_preferencia(carrera: str, preferencia: str):
    result = filter(lambda a: a.Carrera.lower() == carrera.lower() and preferencia.lower() in a.Preferencia.lower(), classmates_list)
    result = list(result)
    return result if result else {"error": "No se encontraron alumnos con esa carrera y preferencia"}

# uvicorn main:app --reload 