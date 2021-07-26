from threading import Thread
from django.core.mail import EmailMessage
from django.conf import settings


class ProductEnquiryThread(Thread):

    def __init__(self, name, phone, email, product_name, product_id, user_name, quantity, recipient):
        Thread.__init__(self)
        self.name = name
        self.phone = phone
        self.email = email
        self.product_name = product_name
        self.product_id = product_id
        self.user_name = user_name
        self.quantity = quantity
        self.recipient = recipient

    def run(self):
        try:
            EmailMessage(
            f'Product Query from {self.name}',
            f'Hi sir, new query from : {self.name}\nPhone : {self.phone}\nEmail : {self.email}\n\nProduct Details :-\nProduct Name : {self.product_name}\nProduct Id : {self.product_id}\nSupplier : {self.user_name}\nQuantity : {self.quantity}',
            settings.EMAIL_HOST_USER,
            self.recipient,
            ).send()

        except:
            pass


class EnquiryThread(Thread):

    def __init__(self, name, email, subject, message, recipient):
        Thread.__init__(self)
        self.name = name
        self.email = email
        self.subject = subject
        self.message = message
        self.recipient = recipient

    def run(self):
        try:
            EmailMessage(
            f'Query from {self.name}',
            f'Hi sir, new query from : {self.name}\nEmail : {self.email}\nSubject : {self.subject}\nMessage : {self.message}',
            settings.EMAIL_HOST_USER,
            self.recipient,
        ).send()

        except:
            pass

