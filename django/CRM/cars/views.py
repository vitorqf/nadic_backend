import uuid
import boto3
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import redirect, render

from CRM.settings import (AWS_ACCESS_KEY_ID, AWS_S3_REGION_NAME,
                          AWS_SECRET_ACCESS_KEY, SQS_QUEUE_URL)

from .forms import CarForm
from .models import Car

sqs = boto3.client(
    "sqs",
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_S3_REGION_NAME,
)


def list_cars(request):
    cars = Car.objects.all()
    messages = retrieve_sqs_messages()
    return render(request, "list_cars.html", {"cars": cars, "messages": messages})

def create_car(request):
    if request.method == "POST":
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                form.save_car()

                message_body = f"Car {form.cleaned_data['plate']} created"
                send_sqs_message(message_body, form.cleaned_data["plate"])

                return redirect("list_cars")

            except IntegrityError:
                return render(
                    request,
                    "create_car.html",
                    {"form": form, "error_message": "Plate already exists"},
                )

    else:
        form = CarForm()

    return render(request, "create_car.html", {"form": form})

def retrieve_sqs_messages():
    response = sqs.receive_message(
        QueueUrl=SQS_QUEUE_URL,
        MaxNumberOfMessages=10,
        AttributeNames=['MessageGroupId', 'MessageDeduplicationId'],
        MessageAttributeNames=['All']
    )


    messages = []
    if "Messages" in response:
        for message in response["Messages"]:
            (message["Attributes"])
            message_body = message["Body"]
            message_group_id = message["Attributes"]["MessageGroupId"]
            message_deduplication_id = message["Attributes"]["MessageDeduplicationId"]
            messages.append(message_body)
            # delete_sqs_message(message["ReceiptHandle"])

    return messages


def send_sqs_message(message_body, message_group_id):
    sqs.send_message(
        QueueUrl=SQS_QUEUE_URL,
        MessageBody=message_body,
        MessageGroupId=message_group_id,
        MessageDeduplicationId=str(uuid.uuid4()),
    )


def delete_sqs_message(receipt_handle):
    sqs.delete_message(
        QueueUrl=SQS_QUEUE_URL,
        ReceiptHandle=receipt_handle,
    )


def get_car_by_id(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        return render(request, "car_by_id.html", {"car": car})

    except Car.DoesNotExist:
        return HttpResponse("Car not found")


def edit_car_by_id(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        if request.method == "POST":
            form = CarForm(request.POST, instance=car)
            if form.is_valid():
                form.update_car(car=car)
                return redirect("list_cars")

        else:
            form = CarForm(instance=car)

        return render(request, "edit_car.html", {"form": form, "car": car})

    except Car.DoesNotExist:
        return HttpResponse("Car not found")


def delete_car_by_id(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        car.delete()
        return redirect("list_cars")

    except Car.DoesNotExist:
        return HttpResponse("Car not found")
