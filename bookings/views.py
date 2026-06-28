import email
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from .models import Booking

# Create your views here.

def booking_success(request):
    reference = request.GET.get('reference')
    return render(request, 'bookings/booking_success.html', {
        'reference': reference
    })


def search_booking(request):
    booking = None
    error = None
    if request.method == "POST":
        reference = request.POST.get("reference", "").strip()
        if reference:
            try:
                booking = Booking.objects.select_related("tour").get(
                    reference__iexact=reference,
                )
            except Booking.DoesNotExist:
                error = "No booking found with that reference number. Please check and try again."
        else:
            error = "Please provide a reference number."
    return render(request, "bookings/search_booking.html", {
        "booking": booking,
        "error": error,
    })


def booking_receipt_pdf(request, reference):
    booking = get_object_or_404(Booking, reference=reference)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = (
        f'attachment; filename="booking_{booking.reference}.pdf"'
    )
    
    from bookings.utils import generate_booking_pdf
    pdf_buffer = generate_booking_pdf(booking)
    response.write(pdf_buffer.read())
    return response