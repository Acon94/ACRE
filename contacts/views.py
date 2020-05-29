from django.shortcuts import render,redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone= request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # check if user has made an  enquiery

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already Submited an enquiery about this property')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id ,name=name,email=email,phone=phone,message=message,user_id=user_id )

        contact.save()

        #send mail 
        send_mail(
            'Property Listing Inquiry ',
            'There has been an inquiry for ' + listing + '. Sign in for more info',
            'achammers0@gmail.com',
            [realtor_email, 'achammers0@gmail.com'],
            fail_silently=False
        )



        messages.success(request,'Youre message has been submitted a realtor will be in touch')
        return redirect('/listings/'+listing_id)
