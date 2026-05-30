from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .models import Tour, Hotel
from bookings.forms import BookingForm 
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings
from bookings.utils import generate_booking_pdf



# def tour_list(request):
#     tours = Tour.objects.all()
#     return render(request, 'tours/tour_list.html', {'tours': tours})


def tour_detail(request, pk):
    tour = get_object_or_404(Tour, pk=pk)
    hotels = tour.hotels.all()

    budget = request.GET.get('budget')

    if budget:
        hotels = hotels.filter(budget_type=budget)

    # ✅ ALWAYS initialize the form
    form = BookingForm()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.tour = tour

             # Prevent duplicate booking
            if booking.__class__.objects.filter(
                tour=tour,
                email=booking.email
            ).exists():
                messages.error(
                    request,
                    "You have already booked this tour using this email."
                )
                return redirect('tour_detail', pk=tour.pk)
            
            booking.save()

            pdf_buffer = generate_booking_pdf(booking)

            email = EmailMessage(
                subject="Your Bena Tours Booking Confirmation",
                body=(
                    f"Hello {booking.full_name},\n\n"
                    f"Your booking was successful!\n\n"
                    f"Reference: {booking.reference}\n"
                    f"Tour: {booking.tour.title}\n\n"
                    f"Please find your receipt attached.\n\n"
                    f"Thank you for choosing Bena Tours."
                ),
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[booking.email],
            )

            

            email.attach(
                f"booking_{booking.reference}.pdf",
                pdf_buffer.read(),
                "application/pdf"
                )
            
        
            email.send()

            # Optional HTML email
            subject = "Booking Confirmation – Bena Tours"
            message = render_to_string(
                'emails/booking_confirmation.html',
                {'booking': booking}
            )

            send_mail(
                    subject,
                    '',
                    settings.DEFAULT_FROM_EMAIL,
                    [booking.email],
                    html_message=message,
                )



            messages.success(
                request,
                f"Booking successful! Your reference number is {booking.reference}. "
                "A confirmation email has been sent."
                )

        
            

                # messages.success(
                #     request,
                #     "Booking successful! A confirmation email has been sent."
                # )
            return redirect('tour_detail', pk=tour.pk)
    # else:
    #     form = BookingForm()

    return render(request, 'tours/tour_detail.html', {
        'tour': tour,
        'form': form,
        'hotels': hotels
    })

def about(request):
     return render(request, "about.html")

    #         booking.save()
    #         return redirect('booking_success')
        
    #     messages.error(request, "There was an error with your booking. Please correct the errors below.")
    

       
    
    
    # return render(request, 'tours/tour_detail.html', {
    #     'tour': tour,
    #     'form': form
    # })


    # return render(request, 'tours/tour_detail.html', {'tour': tour})


def tours(request):
    safari_tours = Tour.objects.filter(category='safari')
    weekend_tours = Tour.objects.filter(category='weekend')

    return render(request, 'tours/tour_list.html', {
        'safari_tours': safari_tours,
        'weekend_tours': weekend_tours
    })

def hotel_detail(request, pk):
    hotel = Hotel.objects.get(id=pk)

    return render(request, 'tours/hotel_detail.html', {
        'hotel': hotel
    })
