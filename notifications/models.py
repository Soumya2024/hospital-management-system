from django.db import models
from core.models import Patient
import uuid
# Create your models here.

class Notification(models.Model):
    notification_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification {self.notification_id} for User {self.user_id}"
       
class NotificationSetting(models.Model):
    setting_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    email_notifications = models.BooleanField(default=True)
    sms_notifications = models.BooleanField(default=False)
    push_notifications = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Settings for User {self.user_id}"
       
class NotificationLog(models.Model):
    log_id = models.AutoField(primary_key=True)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name="logs")
    status = models.CharField(max_length=50)  # e.g., sent, failed, delivered
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log {self.log_id} for Notification {self.notification.notification_id}"
       
class NotificationTemplate(models.Model):
    template_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class ScheduledNotification(models.Model):
    scheduled_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    message = models.TextField()
    scheduled_time = models.DateTimeField()
    sent = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Scheduled Notification {self.scheduled_id} for User {self.user_id}"
       
       
class NotificationChannel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)  # e.g., email, SMS, push
    description = models.TextField(blank=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
       
       
class UserNotificationPreference(models.Model):
    preference_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    channel = models.ForeignKey(NotificationChannel, on_delete=models.CASCADE)
    enabled = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Preferences of {self.user_id} for {self.channel.name}"
       
       
class UserNotificationLog(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=50)
    description = models.TextField()
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.activity_type} at {self.created_at}"
       
class PaitentNotification(models.Model):
    patient_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    paitient_id = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name="patients")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.paitient_id} - {self.patient_id}"