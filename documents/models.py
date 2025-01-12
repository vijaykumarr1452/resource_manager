from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils.http import url_has_allowed_host_and_scheme

def validate_file_size(file):
    max_size = 10 * 1024 * 1024  # 10  MB
    if file.size > max_size:
        raise ValidationError("File size exceeds 10 MB.")

def validate_file_type(file):
    if not file.name.endswith(('.pdf', '.docx', '.xlsx','.ppt')):
        raise ValidationError("Unsupported file type. Allowed types: .pdf, .docx, .xlsx, .ppt.")


class Document(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    doc_url=models.URLField(blank=True,null=True)
    file = models.FileField(upload_to='documents/',validators=[validate_file_size,validate_file_type])
    uploaded_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='documents')

    def __str__(self):
        return self.title




