from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import DocumentForm
from .models import Document

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(document = request.FILES['document'])
            newdoc.uploaded_by = request.user
            newdoc.save()

            return redirect('upload_document')
    else:
        form = DocumentForm()

    documents = Document.objects.filter(uploaded_by=request.user)

    return render(request, '../templates/upload.html', {'form': form, 'documents': documents})

from django.shortcuts import get_object_or_404

@login_required
def delete_document(request, document_id):
    document = get_object_or_404(Document, id=document_id, uploaded_by=request.user)
    document.delete()
    return redirect('upload_document')