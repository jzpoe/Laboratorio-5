// Conectar a MongoDB e insertar documentos
//use Escuela;

// Crear colección e insertar documentos
db.Estudiantes.insertMany([
    { "nombre": "Juan", "edad": 20, "ciudad": "Bogotá" },
    { "nombre": "Ana", "edad": 22, "ciudad": "Medellín" },
    { "nombre": "Luis", "edad": 19, "ciudad": "Cali" }
]);

// Consultar todos los documentos
db.Estudiantes.find();

// Filtrar estudiantes por ciudad
db.Estudiantes.find({ "ciudad": "Bogotá" });

// Consultar estudiantes mayores de 20 años
db.Estudiantes.find({ "edad": { $gt: 20 } });