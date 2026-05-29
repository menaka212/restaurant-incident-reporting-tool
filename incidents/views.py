from django.shortcuts import render, redirect, get_object_or_404
from .models import Incident
from .forms import IncidentForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from stores.models import Store
@login_required
def dashboard(request):

    # Admin can view all incidents
    if request.user.is_superuser:

        incidents = Incident.objects.all()

    # Staff can view only their incidents
    else:

        incidents = Incident.objects.filter(
            created_by=request.user
        )

    total_incidents = incidents.count()
    
    open_incidents = incidents.filter(
        status='Open'
    ).count()

    resolved_incidents = incidents.filter(
        status='Resolved'
    ).count()

    critical_incidents = incidents.filter(
        severity='Critical'
    ).count()
    total_stores = Store.objects.count()
    return render(request, 'dashboard.html', {

        'total_incidents': total_incidents,
        'open_incidents': open_incidents,
        'resolved_incidents': resolved_incidents,
        'critical_incidents': critical_incidents,
        'incidents': incidents,
        'total_stores': total_stores,
    })


@login_required
def create_incident(request):

    if request.method == 'POST':

        form = IncidentForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            incident = form.save(commit=False)

            incident.created_by = request.user

            incident.save()
            messages.success( request, 'Incident created successfully!' )
            return redirect('dashboard')

    else:

        form = IncidentForm()

    return render(request, 'create_incident.html', {
        'form': form
    })


@login_required
def incident_list(request):

    # Admin sees all incidents
    if request.user.is_superuser:

        incidents = Incident.objects.all().order_by(
            '-created_at'
        )

    # Staff sees only their incidents
    else:

        incidents = Incident.objects.filter(
            created_by=request.user
        ).order_by('-created_at')

    category = request.GET.get('category')
    severity = request.GET.get('severity')
    status = request.GET.get('status')

    if category:
        incidents = incidents.filter(category=category)

    if severity:
        incidents = incidents.filter(severity=severity)

    if status:
        incidents = incidents.filter(status=status)

    return render(request, 'incidents.html', {
        'incidents': incidents
    })


@login_required
def update_incident(request, pk):

    # Only admin can update
    if not request.user.is_superuser:

        return redirect('dashboard')

    incident = get_object_or_404(
        Incident,
        id=pk
    )

    form = IncidentForm(
        request.POST or None,
        request.FILES or None,
        instance=incident
    )

    if form.is_valid():

        form.save()
        messages.success( request, 'Incident updated successfully!' )
        return redirect('dashboard')
    
    return render(request, 'update_incident.html', {
        'form': form
    })


@login_required
def delete_incident(request, pk):

    # Only admin can delete
    if not request.user.is_superuser:

        return redirect('dashboard')

    incident = get_object_or_404(
        Incident,
        id=pk
    )

    incident.delete()

    messages.success( request, 'Incident deleted successfully!' )
    return redirect('dashboard')

from django.core.management import call_command
from django.http import HttpResponse

def load_data(request):
    call_command('loaddata', 'data.json')
    return HttpResponse("Data Loaded Successfully")
