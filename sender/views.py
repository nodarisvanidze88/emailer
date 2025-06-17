from django.http import HttpResponse
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
@api_view(['GET'])
def status_ok(request):
    """
    View to return a simple 'OK' response.
    """
    return Response({'status': 'OK'})

@api_view(['POST'])
def email_sender(request):
    """
    View to handle sending an email.
    This is a placeholder function; actual email sending logic should be implemented here.
    """
    # Extract data from the request
    data = request.data
    email_receipient = data.get('recipient')
    email_subject = data.get('subject')
    email_body = data.get('body')
    if not email_receipient or not email_subject or not email_body:
        return Response({'error': 'Missing required fields'}, status=400)
    try:
        send_mail(
            email_subject,
            email_body,
            settings.DEFAULT_FROM_EMAIL,
            [email_receipient],
            fail_silently=False,
        )
    except Exception as e:
        return Response({'error': str(e)}, status=500)

    return Response({'message': 'Email sent successfully!', 'data': data})