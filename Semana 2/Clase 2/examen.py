#ejercio 5: mostrar si un estudiante esta habilitado patra presentar el examen
    #si el estudiante fue a mas del 75% de las clases puede hacer el examen
    #si tiene menos del 75 % solo puede hacer el examen con excusa medica

numeroClases = int(input("Por favor ingrese el número de clases del curso: "))
clasesAsistidas = int(input("Por favor ingrese el número de clases a las que asistió el estudiante: "))

porcentajeAsistencia = clasesAsistidas / numeroClases

if porcentajeAsistencia > 0.75:
    print("El estudiante puede presentar el examen su asistencia fue de {:.2f}%".format(porcentajeAsistencia*100))
else:
    tieneExcusa = input("El estudiante tiene excusa médica?: ").lower()
    if tieneExcusa == "si" or tieneExcusa == "sí":
        print("El estudiante puede presentar el examen")
    else:
        print("El estudiante NO puede presentar el examen, su asistencia fue de {:.2f}%".format(porcentajeAsistencia*100))


