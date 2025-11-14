from django.shortcuts import render

# Define la vista para la página de inicio
def inicio(request):
    # La ruta es relativa a la carpeta 'templates'.
    # Busca 'mi_app/index.html' dentro de 'templates/'.
    return render(request, 'mi_app/index.html')