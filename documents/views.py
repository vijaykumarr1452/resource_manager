from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,render,redirect
from .models import Document
from .forms import DocumentForm

# List documents uploaded by the logged-in-user

@login_required
def document_list(request):
    documents = Document.objects.filter(user=request.user)
    return render(request, 'documents/document_list.html', {'documents': documents})

@login_required
def document_detail(request, pk):
    document = Document.objects.get(pk=pk, user=request.user)
    return render(request, 'documents/document_detail.html', {'document': document})

@login_required
def document_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.user = request.user
            document.save()
            return redirect('document_list')
        else:
            form = DocumentForm()
    return render(request, 'documents/document_upload.html', {'form': form})
