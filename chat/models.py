from django.db import models
from core.models import Patient, Staff
import uuid
# Create your models here.

class ChatSession(models.Model):
    session_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Session {self.session_id} for User {self.user_id}"
# ===================================================================================
# -----------------------------------------
# Message
# -----------------------------------------
class Message(models.Model):
    message_id = models.AutoField(primary_key=True)
    session = models.ForeignKey(ChatSession, on_delete=models.CASCADE, related_name="messages")
    sender = models.CharField(max_length=50)  # e.g., 'user' or 'bot'
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Message {self.message_id} in Session {self.session.session_id} by {self.sender}"
# -----------------------------------------  
# Patient
# -----------------------------------------
class Patient(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="appointments")
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="appointments")
    appointment_date = models.DateTimeField()
    reason = models.TextField()
    status = models.CharField(max_length=50, default='scheduled')  # e.g., scheduled, completed, canceled
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return f"Appointment {self.appointment_id} for Patient {self.patient.patient_id} with Staff {self.staff.staff_id}"

class PatientRecord(models.Model):
    record_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="medical_records")
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, related_name="created_records")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"Record {self.record_id} for Patient {self.patient.patient_id} by Staff {self.staff.staff_id}"

class Collection(models.Model):
    collection_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# -----------------------------------------
# Document
# -----------------------------------------
class Document(models.Model):
    document_id = models.AutoField(primary_key=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE, related_name="documents")
    title = models.CharField(max_length=255)
    content = models.TextField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title