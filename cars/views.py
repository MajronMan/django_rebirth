from django.shortcuts import render
from io import BytesIO
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def some_view(request):
    # Create the HttpResponse object with the appropriate PDF headers.
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pdf_przyklad.pdf"'

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response,initialFontName='Times-Roman')

    #List of application's fields
    NAME = "Jan Nowak"

    p.showPage()
    p.save()
    return response

# Create your views here.
