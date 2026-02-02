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
    return render(request, 'bookings/booking_success.html')


def search_booking(request):
    booking = None
    error = None

    if request.method == "POST":
        reference = request.POST.get("reference", "").strip()

        if reference:
            try:
                booking = Booking.objects.select_related("tour").get(
                    reference__iexact=reference,
                    email__iexact=email
                )
            except Booking.DoesNotExist:
                error = "No booking found with that reference number."

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

    doc = SimpleDocTemplate(response, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    # Title
    elements.append(Paragraph("BENA TOURS – BOOKING RECEIPT", styles['Title']))
    elements.append(Spacer(1, 20))

    # Booking info table
    data = [
        ["Reference Number", booking.reference],
        ["Full Name", booking.full_name],
        ["Email", booking.email],
        ["Phone", booking.phone],
        ["Tour", booking.tour.title],
        ["Persons", booking.persons],
        ["Booking Date", booking.booked_on.strftime("%d %b %Y %H:%M")],
    ]

    table = Table(data, colWidths=[150, 300])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('FONT', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 30))

    elements.append(
        Paragraph(
            "Thank you for booking with Bena Tours. "
            "Please keep this receipt for your records.",
            styles['Normal']
        )
    )

    doc.build(elements)
    return response
