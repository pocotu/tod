from django.shortcuts import render

def horario(request):
  """
  Renderiza el horario de clases.

  Args:
    request: Una solicitud HTTP.

  Returns:
    Una respuesta HTTP.
  """

  courses = get_courses()
  schedule = generate_schedule(courses)

  return render(request, 'horario.html', {'schedule': schedule})
