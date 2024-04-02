from django.shortcuts import render,redirect
from django.db import connection
from .models import Sedes, Doctores, Pacientes
# Create your views here.
def index(request):
    return render(request,'index.html')

# Página formulario sede
def formSede(request): 
    if request.method == 'POST':
        # Guarda los datos enviados
        nombre_s = request.POST.get('nombre_s')
        horario_s = request.POST.get('horario_s')
        ubicacion_s = request.POST.get('ubicacion_s')
        # Verifica si existen todos
        if nombre_s and horario_s and ubicacion_s:
            # Agrega la variable activo
            activo_s = "Activo"
            # Envia los datos con un call al procedimiento en bd
            sedes = connection.cursor()
            sedes.execute(" call agregarSede('"+nombre_s+"','"+horario_s+"','"+ubicacion_s+"','"+activo_s+"')")
            env = "Se ha enviado correctamente"
            return render(request,'Sedes/formSede.html', {
                'env':env,
            })
        else:
            env = "No se ha podido enviar correctamente"
            return render(request,'Sedes/formSede.html', {
                'env':env,
            })  
    else: 
        return render(request,'Sedes/formSede.html')
    
# Página editar formulario sede   
def editSede(request,id): 
    if request.method == 'POST':
        nombre_s = request.POST.get('nombre_s')
        horario_s = request.POST.get('horario_s')
        ubicacion_s = request.POST.get('ubicacion_s')
        if nombre_s and horario_s and ubicacion_s:
            sede = connection.cursor()
            sedes = connection.cursor()
            sede.execute(" call actualizarSede('"+str(id)+"','"+nombre_s+"','"+horario_s+"','"+ubicacion_s+"')")
            sedes.execute("call editSede('"+str(id)+"')")
            editar = sedes.fetchall()
            env = "Se ha enviado correctamente"
            return render(request,'Sedes/editSede.html',{
            'editar':editar,
            'env':env,
            })
        else:
            sedes = connection.cursor()
            sedes.execute("call editSede('"+str(id)+"')")
            editar = sedes.fetchall()
            env = "No se ha podido enviar correctamente, verifica los datos"
            return render(request,'Sedes/editSede.html',{
            'editar':editar,
            'env':env,
            })
    else:
       sede = connection.cursor()
       sede.execute("call editSede('"+str(id)+"')")
       editar = sede.fetchall()
       return render(request,'Sedes/editSede.html',{
           'editar': editar,
       })

# Listado Activos Sede
def listadoSedeA(request):
    sedes = connection.cursor()
    sedes.execute("call listaSedesA()")
    lista_sedes = sedes.fetchall()
    return render(request, 'Sedes/listaSedeA.html',{
        "sedes":lista_sedes,
    })
    
# Listado Inactivos Sede
def listadoSedeI(request):
    sedes = connection.cursor()
    sedes.execute("call listaSedesI()")
    lista_sedes = sedes.fetchall()
    return render(request, 'Sedes/listaSedeI.html',{
        "sedes":lista_sedes,
    })

# Inactivar Sede
def listadoInactivar(request, id):
    sede = connection.cursor()
    sede.execute("call sedeInactivar('"+str(id)+"')")
    print(id)
    return redirect("/listadosedeA")

# Activar Sede
def listadoActivar(request, id):
    sede = connection.cursor()
    sede.execute("call sedeActivar('"+str(id)+"')")
    print(id)
    return redirect("/listadosedeI")


# Página formulario doctores
def formDoctores(request):
    sedes = Sedes.objects.filter(activo_s="Activo")
    if request.method == 'POST':
        identificacion_d = request.POST.get('identificacion_d')
        nombres_d = request.POST.get('nombres_d')
        apellidos_d = request.POST.get('apellidos_d')
        correo_d = request.POST.get('correo_d')
        direccion_d =request.POST.get('direccion_d')
        telefono_d = request.POST.get('telefono_d')
        foto_d = request.FILES.get('foto_d')
        sede_d = request.POST.get('sede_d')
        if identificacion_d and nombres_d and apellidos_d and correo_d and direccion_d and telefono_d and sede_d and foto_d:
            insertSede = Sedes.objects.get(id=int(sede_d))
            doctor = Doctores()
            doctor.identificacion_d = identificacion_d
            doctor.nombres_d = nombres_d
            doctor.apellidos_d = apellidos_d
            doctor.correo_d = correo_d
            doctor.direccion_d = direccion_d
            doctor.telefono_d = telefono_d
            doctor.foto_d = foto_d
            doctor.sede_d = insertSede
            doctor.activo_d = "Activo"
            doctor.save()
            return redirect('/')
        else:
            return render(request,'Doctores/formDoctores.html')
    else:   
        return render(request,'Doctores/formDoctores.html',{
            'sedes': sedes,
        })

# Página editar formulario doctores
def editDoctores(request,id):
    sedes = Sedes.objects.all()
    # sedes = Sedes.objects.filter(activo_s="Activo")
    doctores = Doctores.objects.filter(id=id)
    if request.method == 'POST':
        identificacion_d = request.POST.get('identificacion_d')
        nombres_d = request.POST.get('nombres_d')
        apellidos_d = request.POST.get('apellidos_d')
        correo_d = request.POST.get('correo_d')
        direccion_d =request.POST.get('direccion_d')
        telefono_d = request.POST.get('telefono_d')
        foto_d = request.FILES.get('foto_d')
        sede_d = request.POST.get('sede_d')
        if id and identificacion_d and nombres_d and apellidos_d and correo_d and direccion_d and telefono_d and sede_d:
            insertSede = Sedes.objects.get(id=int(sede_d))
            doctor = Doctores.objects.get(id=id)
            if foto_d:
                doctor.foto_d.delete()
                doctor.foto_d = foto_d
            doctor.identificacion_d = identificacion_d
            doctor.nombres_d = nombres_d
            doctor.apellidos_d = apellidos_d
            doctor.correo_d = correo_d
            doctor.direccion_d = direccion_d
            doctor.telefono_d = telefono_d
            doctor.sede_d = insertSede
            doctor.activo_d = "Activo"
            doctor.save()
            env = "Se ha enviado correctamente"
            return render(request,'Doctores/editDoctores.html',{
                'env':env,
                'sedes': sedes,
                'doctores':doctores,
            })
        else:
            env = "No se ha podido enviar correctamente, verifica los datos"
            return render(request,'Doctores/editDoctores.html',{
                'env':env,
                'sedes': sedes,
                'doctores':doctores,
            })
    else:   
        return render(request,'Doctores/editDoctores.html',{
            'sedes': sedes,
            'doctores':doctores,
        })
        
# Listado Activos
def listadoDoctoresA(request):
    doctores = Doctores.objects.filter(activo_d="Activo")
    return render(request, 'Doctores/listaDoctoresA.html',{
        "doctores":doctores,
    })
    
# Listado Inactivos
def listadoDoctoresI(request):
    doctores = Doctores.objects.filter(activo_d="Inactivo")
    return render(request, 'Doctores/listaDoctoresI.html',{
        "doctores":doctores,
    })

# Inactivar doctor
def listDocInactivar(request, id):
    doctor = Doctores.objects.get(id=id)
    doctor.activo_d = "Inactivo"
    doctor.save()
    return redirect("/listadodoctoresA")

# Activar doctor
def listDocActivar(request, id):
    doctor = Doctores.objects.get(id=id)
    doctor.activo_d = "Activo"
    doctor.save()
    return redirect("/listadodoctoresI")

# Página formulario pacientes
def formPacientes(request):
    sedes = Sedes.objects.filter(activo_s="Activo")
    doctores = Doctores.objects.filter(activo_d="Activo")
    if request.method == 'POST':
        identificacion_p = request.POST.get('identificacion_p')
        nombres_p = request.POST.get('nombres_p')
        apellidos_p = request.POST.get('apellidos_p')
        correo_p = request.POST.get('correo_p')
        edad_p = request.POST.get('edad_p')
        direccion_p =request.POST.get('direccion_p')
        telefono_p = request.POST.get('telefono_p')
        foto_p = request.FILES.get('foto_p')
        sede_p = request.POST.get('sede_p')
        doctor_p = request.POST.get('doctor_p')
        if identificacion_p and nombres_p and apellidos_p and correo_p and edad_p and direccion_p and telefono_p and sede_p and foto_p and doctor_p:
            insertSede = Sedes.objects.get(id=int(sede_p))
            insertDoctor = Doctores.objects.get(id=int(doctor_p))
            paciente = Pacientes()
            paciente.identificacion_p = identificacion_p
            paciente.nombres_p = nombres_p
            paciente.apellidos_p = apellidos_p
            paciente.correo_p = correo_p
            paciente.edad_p = edad_p
            paciente.direccion_p = direccion_p
            paciente.telefono_p = telefono_p
            paciente.foto_p = foto_p
            paciente.sede_p = insertSede
            paciente.doctor_p = insertDoctor
            paciente.activo_p = "Activo"
            paciente.save()
            return redirect('/')
        else:
            return render(request,'Pacientes/formPacientes.html')
    else:   
        return render(request,'Pacientes/formPacientes.html',{
            'sedes': sedes,
            'doctores': doctores,
        })

# Página editar formulario pacientes
def editPacientes(request,id):
    sedes = Sedes.objects.all()
    doctores = Doctores.objects.all()
    # sedes = Sedes.objects.filter(activo_s="Activo")
    # doctores = Doctores.objects.filter(activo_d="Activo")
    pacientes = Pacientes.objects.filter(id=id)
    if request.method == 'POST':
        identificacion_p = request.POST.get('identificacion_p')
        nombres_p = request.POST.get('nombres_p')
        apellidos_p = request.POST.get('apellidos_p')
        correo_p = request.POST.get('correo_p')
        edad_p = request.POST.get('edad_p')
        direccion_p =request.POST.get('direccion_p')
        telefono_p = request.POST.get('telefono_p')
        foto_p = request.FILES.get('foto_p')
        sede_p = request.POST.get('sede_p')
        doctor_p = request.POST.get('doctor_p')
        if identificacion_p and nombres_p and apellidos_p and correo_p and edad_p and direccion_p and telefono_p and sede_p and doctor_p:
            insertSede = Sedes.objects.get(id=int(sede_p))
            insertDoctor = Doctores.objects.get(id=int(doctor_p))
            paciente = Pacientes.objects.get(id=id)
            if foto_p:
                paciente.foto_p.delete()
                paciente.foto_p = foto_p
            paciente.identificacion_p = identificacion_p
            paciente.nombres_p = nombres_p
            paciente.apellidos_p = apellidos_p
            paciente.correo_p = correo_p
            paciente.edad_p = edad_p
            paciente.direccion_p = direccion_p
            paciente.telefono_p = telefono_p
            paciente.sede_p = insertSede
            paciente.doctor_p = insertDoctor
            paciente.activo_p = "Activo"
            paciente.save()
            env = "Se ha enviado correctamente"
            return render(request,'Pacientes/editPacientes.html',{
                'env':env,
                'sedes': sedes,
                'doctores':doctores,
                'pacientes':pacientes,
            })
        else:
            env = "No se ha podido enviar correctamente, verifica los datos"
            return render(request,'Pacientes/editPacientes.html',{
                'env':env,
                'sedes': sedes,
                'doctores':doctores,
                'pacientes':pacientes,
            })
    else:   
        return render(request,'Pacientes/editPacientes.html',{
            'sedes': sedes,
            'doctores':doctores,
            'pacientes':pacientes,
            
        })
        
# Listado Activos
def listadoPacientesA(request):
    pacientes = Pacientes.objects.filter(activo_p="Activo")
    return render(request, 'Pacientes/listaPacientesA.html',{
        "pacientes":pacientes,
    })
    
# Listado Inactivos
def listadoPacientesI(request):
    pacientes = Pacientes.objects.filter(activo_p="Inactivo")
    return render(request, 'Pacientes/listaPacientesI.html',{
        "pacientes":pacientes,
    })

# Inactivar paciente
def listPacInactivar(request, id):
    paciente = Pacientes.objects.get(id=id)
    paciente.activo_p = "Inactivo"
    paciente.save()
    return redirect("/listadopacientesA")

# Activar paciente
def listPacActivar(request, id):
    paciente = Pacientes.objects.get(id=id)
    paciente.activo_p = "Activo"
    paciente.save()
    return redirect("/listadopacientesI")