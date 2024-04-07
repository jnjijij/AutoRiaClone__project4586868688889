from backend.configs import models



class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
          return self.title

class NotificationManager:
    @staticmethod
    def send_notification(user, message):
        Notification.objects.create(user=user, message=message)
