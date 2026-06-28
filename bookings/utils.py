from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

def generate_booking_pdf(booking):
    buffer = BytesIO()
    doc = SimpleDocTemplate(
        buffer, 
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40
    )
    styles = getSampleStyleSheet()
    elements = []

    # ── HEADER ──
    header_style = ParagraphStyle(
        'Header',
        fontSize=22,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#1a6b3c'),
        alignment=1,  # Center
        spaceAfter=4,
    )
    subheader_style = ParagraphStyle(
        'SubHeader',
        fontSize=11,
        fontName='Helvetica',
        textColor=colors.HexColor('#555555'),
        alignment=1,
        spaceAfter=20,
    )

    elements.append(Paragraph("🌍 QuintessentialSafaris", header_style))
    elements.append(Spacer(1, 10))

    # ── DIVIDER ──
    elements.append(HRFlowable(
        width="100%", 
        thickness=2, 
        color=colors.HexColor('#1a6b3c')
    ))
    elements.append(Spacer(1, 10))

    # ── RECEIPT TITLE ──
    title_style = ParagraphStyle(
        'Title',
        fontSize=14,
        fontName='Helvetica-Bold',
        textColor=colors.HexColor('#333333'),
        alignment=1,
        spaceAfter=15,
    )
    elements.append(Paragraph("BOOKING RECEIPT", title_style))
    elements.append(Spacer(1, 10))

    # ── BOOKING DETAILS TABLE ──
    data = [
        ["Reference Number", booking.reference],
        ["Full Name", booking.full_name],
        ["Email", booking.email],
        ["Phone", booking.phone],
        ["Tour", booking.tour.title],
        ["Number of Persons", str(booking.persons)],
        ["Booking Date", booking.booked_on.strftime("%d %b %Y %H:%M")],
    ]

    table = Table(data, colWidths=[180, 310])
    table.setStyle(TableStyle([
        # Header column styling
        ('BACKGROUND', (0, 0), (0, -1), colors.HexColor('#1a6b3c')),
        ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),

        # Value column styling
        ('BACKGROUND', (1, 0), (1, -1), colors.HexColor('#f9f9f9')),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#333333')),

        # Alternating row colors
        ('BACKGROUND', (1, 1), (1, 1), colors.HexColor('#f0f0f0')),
        ('BACKGROUND', (1, 3), (1, 3), colors.HexColor('#f0f0f0')),
        ('BACKGROUND', (1, 5), (1, 5), colors.HexColor('#f0f0f0')),

        # Grid and padding
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#cccccc')),
        ('PADDING', (0, 0), (-1, -1), 10),
        ('ROWBACKGROUND', (0, 0), (-1, -1), [colors.white]),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ]))

    elements.append(table)
    elements.append(Spacer(1, 20))

    # ── THANK YOU MESSAGE ──
    thank_you_style = ParagraphStyle(
        'ThankYou',
        fontSize=11,
        fontName='Helvetica',
        textColor=colors.HexColor('#333333'),
        alignment=1,
        spaceAfter=10,
    )
    elements.append(Paragraph(
        "Thank you for choosing QuintessentialSafaris!",
        thank_you_style
    ))
    elements.append(Paragraph(
        "Please keep this receipt for your records.",
        thank_you_style
    ))

    elements.append(Spacer(1, 20))

    # ── DIVIDER ──
    elements.append(HRFlowable(
        width="100%",
        thickness=1,
        color=colors.HexColor('#1a6b3c')
    ))
    elements.append(Spacer(1, 10))

    # ── FOOTER ──
    footer_style = ParagraphStyle(
        'Footer',
        fontSize=9,
        fontName='Helvetica',
        textColor=colors.HexColor('#888888'),
        alignment=1,
        spaceAfter=4,
    )
    elements.append(Paragraph(
        "QuintessentialSafaris | quintessentialsafarisltd@gmail.com | +254 724852418",
        footer_style
    ))
    elements.append(Paragraph(
        "www.quintessential-safaris-1.onrender.com",
        footer_style
    ))
    elements.append(Paragraph(
        "© QuintessentialSafaris. All rights reserved.",
        footer_style
    ))

    doc.build(elements)
    buffer.seek(0)
    return buffer
