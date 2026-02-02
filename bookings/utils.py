from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

def generate_booking_pdf(booking):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("BENA TOURS – BOOKING RECEIPT", styles['Title']))
    elements.append(Spacer(1, 20))

    data = [
        ["Reference", booking.reference],
        ["Full Name", booking.full_name],
        ["Email", booking.email],
        ["Phone", booking.phone],
        ["Tour", booking.tour.title],
        ["Persons", booking.persons],
        ["Date", booking.booked_on.strftime("%d %b %Y %H:%M")],
    ]

    table = Table(data, colWidths=[150, 300])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, -1), colors.lightgrey),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey),
        ('PADDING', (0, 0), (-1, -1), 8),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))
    elements.append(
        Paragraph(
            "Thank you for booking with Bena Tours.",
            styles['Normal']
        )
    )

    doc.build(elements)
    buffer.seek(0)
    return buffer
